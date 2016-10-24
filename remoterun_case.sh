#!/bin/bash
name=$1
rc()
{
	echo -e "\033[31m$str\033[0m"  #print the string with red color
}
yc()
{
	echo -e "\033[33m$str\033[0m"  #print the string with yellow color
}
remote_copy()
{
        for i in `seq 1 4`
        do
		str="12cnode$i"
		rc $str
                if [ -f $file ]
                then
                        scp $file 12cnode$i:$file
                fi
        done
}
remote_command()
{
	for i in `seq 1 4`
        do
		str="12cnode$i"
		rc $str
                ssh 12cnode$i $cmd
        done
}
remote_script()
{
	for i in `seq 1 4`
        do
		str="12cnode$i"
		rc $str
                scp $script 12cnode$i:$script
                ssh 12cnode$i sh $script
                echo "12cnode$i script finished"
        done
}

usage()
{
	echo "remoterun [-option] [file|command]"
	echo "-h,--help,print usage"
	echo "-c,--copy <file on local path>,copy local file to remote nodes"
	echo "-cmd,--command <shell command>,excute shell command on node list"
	echo "-s,--script <script_full_path>,excute local script on node list"
	echo "-n,--node ,It's used for after 3 option above is about just excute on specify node"
}
################main##############

case "$name" in
	--copy|-c)
		str="start copy file to remote nodes"
		yc $str
		file=$2
		if [ x$3 != x ]
		then
			if [ $3 == "--node" -o  $3 ==  "-n" ]
			then
				host=$4
				str="$host"
				rc $str
				scp $file $host:$2	
				str="Copy $file to remote node $host successfully"
				yc $str
			fi
		else
			remote_copy $file #call remote copy function
			str="Copy $file to remote nodes successfully"
			yc $str 
		fi
	;;
	--command|-cmd)
		str="Command start"
		yc $str
		cmd=$2
		if [ x$3 != x ]
		then
			if [ $3 == "--node" -o  $3 ==  "-n" ]
			then #should add verify wheather the node is existing
				host=$4
				str=$host
				rc $str
        	        	ssh $4 $cmd	
				str="Command $cmd excution on remote node $host successfully"
				yc $str
			fi
		else
			remote_command  $cmd  #excute remote command
			str="Command $cmd excution on remote nodes successfully"
			yc $str
		fi
	;;
	--script|-s)
		str="Script start"
		rc $str
		script=$2
		if [ x$3 != x ]
		then
			if [ $3 == "--node" -o  $3 ==  "-n" ]
			then
				host=$4
				str="$host"
				rc $str
				ssh $host sh $script	
				str="Script $scrint excution on remote node $host successfully"
				yc $str
			fi
		else
			remote_script $script #call remote copy function
			str="Script $cmd excution on remote nodes successfully"
			yc $str
		fi
	;;
	*)
		usage	
	;;
esac
