     #!/bin/bash

     while IFS= read -r project_url
     do
         git clone "$project_url"
     done < C:/Users/Ана/Desktop/ДИПЛОМ/itis_files/web_urls.txt
     
