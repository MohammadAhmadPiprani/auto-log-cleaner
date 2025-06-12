import os, time
log_folder= "log"
check_min=1
check_int_sec=2
while True:
    print("Its checking the files")
    if os.path.exists(log_folder):
        current_time= time.time()
        for file in os.listdir(log_folder):
            file_path= os.path.join(log_folder,file)
            if os.path.isfile(file_path):
                total_sec= current_time - os.path.getmtime(file_path)
                total_min= total_sec / 60
                if total_min > check_min:
                    print("Files are deleting")
                    os.remove(file_path)
        print("waiting for next")
    else:
        print("No folder found")
    time.sleep(check_int_sec)
    

            
        
        

    
 