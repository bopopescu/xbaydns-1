#!/bin/sh

PPATH=`dirname $0`
if [ -f "$PPATH/../agent.conf" ]; then
	. $PPATH/../agent.conf
fi

cd $PPATH
rsync -avz -e 'ssh -i /home/xdagent/rsync-key' \
 xbaydns\@$MASTER_IP:/home/xbaydns/iplist ../iplist

