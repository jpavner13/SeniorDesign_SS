# SeniorDesign_SS
This repository holds all of the code for senior design 2024/2025

 - Download VSCode
 - Download Docker Desktop as in the previous post
 - Download the Docker extension from the extensions tab in VSCode
 - Clone the github at "https://github.com/jpavner13/SeniorDesign_SS"
 - In VSCode open the project folder
    - It will prompt you to "Reopen in Container." DO NOT REOPEN IN CONTAINER!!!!!!
  - Select the Docker extension tab on the left hand side, next to containers press the + sign, then "Open Current Folder in Container." 
    - The first time your computer builds the container it will take a while, you can press "show logs" to see its process.
  - Once the container is opened, it will prompt you to authenticate your GitHub in the Terminal.
    - Select GitHub.com
    - Select HTTPS
    - Enter 'Y'
    - Select Login with a web browser
    - Copy the one-time code that is given to you, then press Enter
      - If it fails, enter the URL into a browser manually
    - Enter the one-time code that was given to you
    - Select "Authorize GitHub" and Login
    - Return to VSCode and make sure it is successful, press any key to continue
  - Now you are in the project virtual enviornment logged in as yourself. This process will only need to be repeated when the container needs to be rebuilt. This may happen a few more times during the semester.
  - Use the built in "Source Control" extension in VSCode to manage branch and version control
