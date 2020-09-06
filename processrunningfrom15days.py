#5 min old Processes
ps -eo comm,pid,etimes | awk '/^procname/ {if ($3 > 300) { print $2}}'

#5/10/15 Days old Processes

echo '5 Days Old Processes'
ps -eo pid,etime,comm | awk '$2~/^5-/ && $3~/mycommand/ { print $1 }'
echo '10 Days Old Processes'
ps -eo pid,etime,comm | awk '$2~/^10-/ && $3~/mycommand/ { print $1 }'
echo '15 Days Old Processes'
ps -eo pid,etime,comm | awk '$2~/^15-/ && $3~/mycommand/ { print $1 }'
