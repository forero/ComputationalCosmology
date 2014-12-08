from subprocess import call
import os.path

def data_base_query(query, outputfile, password="42", username="forero"):
    website = "http://wget.multidark.org/MyDB?action=doQuery&SQL="
    wget_options="--auth-no-challenge --content-disposition --cookies=on --keep-session-cookies --save-cookies=cookie.txt --load-cookies=cookie.txt" 
    wget_options=wget_options+" -O "+outputfile +" "
    wget_command="wget --http-user="+username+" --http-passwd="+password+" "+wget_options
    command = wget_command + "\""+ website + query+"\""
    #print command
    retcode = call(command,shell=True)


query = "SELECT top 10 * FROM miniMDR1..FOF WHERE snapnum=85  ORDER BY mass desc"
output_file = "test_file.csv"
n = data_base_query(query, output_file, password="lapiz5borra")
