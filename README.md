<h1 align="center">Python Algorithm for User Access Management</h1>
This project demonstrates an algorithm developed in Python to manage a list of authorized users who have access to sensitive data based on IP addresses. The script automates the process of removing users who no longer have access and adding new users who now have access.<br/> 

<h2>Objective</h2>
Create a Python function that updates a user access file by removing users who no longer have access and adding those who now have access based on their IP addresses.

<h2>Project Overview</h2>
In this project, I simulate the role of a security analyst at a hospital who is responsible for maintaining a list of employees authorized to access sensitive patient information (SPII). Access is determined by a list of allowed IP addresses. The script reads from an existing file of authorized users, compares it with a "remove list," and automatically updates the file by adding or removing users accordingly.


<p align="center" style="margin-top: 10px;">
  <img src="https://github.com/user-attachments/assets/f2cb8cdb-3643-4144-a420-85d045f91633" alt="Image Description" width="400"/>
</p>


<h2>Steps: Creating the Script</h2>

<h3>Step 1 - Define Function <code>update_file(import_file, remove_list)</code></h3>
<p>
The first step is to define the function <code>update_file()</code>. I am using two parameters: <code>import_file</code> and <code>remove_list</code>. These are the two important elements needed to remove any users who no longer have access.
</p>

<p align="center" style="margin-top: 10px;">
  <img src="https://github.com/user-attachments/assets/5f2fb696-67c8-4d9c-ba6d-e682469b3a3f" alt="Image Description" width="400"/>
</p>

<h3>Step 2 - Open the file that contains the allow list</h3>
<p>
Using the <code>open()</code> function, I define two arguments: the variable <code>import_file</code> and the second argument, "r", signifying that I want the function to read the file. Then, I assign it to a variable called <code>file</code>.
</p>

<p align="center" style="margin-top: 10px;">
  <img src="https://github.com/user-attachments/assets/7824d73c-fbe5-4edf-9839-60523cbcd960" alt="Image Description" width="400"/>
</p>

<h3>Step 3 - Read the file contents and convert them into a string</h3>
<p>
Next, I create a new variable within my function called <code>ip_addresses</code>; this is essentially my list. I call the <code>.read()</code> method on the variable <code>file</code> to convert the file content into a string, allowing me to manipulate it further.
</p>

<p align="center" style="margin-top: 10px;">
  <img src="https://github.com/user-attachments/assets/eea0e2a1-6d1e-41a8-95c4-6cfa8c7272d4" alt="Image Description" width="400"/>
</p>


<h3>Step 4 - Convert the string into a list</h3>
<p>
Now that the variable <code>ip_addresses</code> is a string, I can convert it into a list. I apply the <code>.split()</code> method to <code>ip_addresses</code>, which splits the string whenever it encounters whitespace, creating a list of IP addresses.
</p>

<p align="center" style="margin-top: 10px;">
  <img src="https://github.com/user-attachments/assets/551f0df5-e79e-4849-8a22-1f9b27c94444" alt="Image Description" width="400"/>
</p>

<h3>Step 5 - Iterate through the remove list</h3>
<p>
I create a loop that goes through each item in <code>ip_addresses</code>. Using <code>for element in ip_addresses:</code>, I set up the loop to check each IP address.
</p>

<p align="center" style="margin-top: 10px;">
  <img src="https://github.com/user-attachments/assets/f446a2f0-8684-41c3-9fac-58042f488d1c" alt="Image Description" width="400"/>
</p>

<h3>Step 6 - Remove IP addresses that are on the remove list</h3>
<p>
For each IP address in <code>ip_addresses</code>, I check if it is in the <code>remove_list</code> using an <code>if</code> statement. If the IP matches one in the removal list, it is removed using the <code>.remove()</code> method.
</p>

<p align="center" style="margin-top: 10px;">
  <img src="https://github.com/user-attachments/assets/f57cc208-349c-43f7-8a26-95eb8ddfbfc7" alt="Image Description" width="400"/>
</p>

<h3>Step 7 - Update the file with the revised list of IP addresses</h3>
<p>
I then combine the elements within <code>ip_addresses</code> back into a single string. I do this using the <code>.join()</code> method, separating each address with a space.
</p>

<p align="center" style="margin-top: 10px;">
  <img src="https://github.com/user-attachments/assets/0aaf8c3a-e90c-41c5-90bb-dfd0d0e3b8f5" alt="Image Description" width="400"/>
</p>

<h3>Step 8 - Re-open the file and overwrite it</h3>
<p>
To finish updating the file, I open <code>import_file</code> again in write mode ("w"). Using the <code>.write()</code> method, I overwrite the file with the updated list of IP addresses.
</p>

<p align="center" style="margin-top: 10px;">
  <img src="https://github.com/user-attachments/assets/9b63bb02-9876-4dbf-a614-c42e9816120d" alt="Image Description" width="400"/>
</p>

<h3>Step 9 - Assign variables and call the function</h3>
<p>
In this final step, I define two variables: <code>import_file</code> and <code>remove_list</code>. The <code>import_file</code> contains the file to be updated, while <code>remove_list</code> specifies the IP addresses to be removed. I then call the function <code>update_file(import_file, remove_list)</code>.
</p>

<p align="center" style="margin-top: 10px;">
  <img src="https://github.com/user-attachments/assets/31e7fbdd-407d-4142-8fc9-8fbbb875efce" alt="Image Description" width="600"/>
</p>

<p>
Finally, to verify that the function worked correctly, I re-open the updated file in read mode and print its contents. This allows me to visually confirm that the specified IP addresses have been removed.
</p>

<h2>Summary of Python Skills Used</h2>
<ul>
  <li><strong>Define Function:</strong> Created a function <code>update_file()</code> with parameters <code>import_file</code> and <code>remove_list</code>.</li>
  <li><strong>Read File:</strong> Opened <code>import_file</code> in read mode and read its contents into the variable <code>ip_addresses</code>.</li>
  <li><strong>Split Content:</strong> Converted the string <code>ip_addresses</code> into a list of IP addresses using the <code>.split()</code> method.</li>
  <li><strong>Remove IPs:</strong> Looped through each element in <code>ip_addresses</code> and removed any that matched an IP in <code>remove_list</code>.</li>
  <li><strong>Join Content:</strong> Joined the updated list of IP addresses back into a single string separated by spaces.</li>
  <li><strong>Write File:</strong> Opened <code>import_file</code> in write mode and wrote the updated string of IP addresses back into the file.</li>
  <li><strong>Call Function:</strong> Called the <code>update_file()</code> function with <code>import_file</code> set to 'allowed_list.txt' and <code>remove_list</code> containing the IPs to be removed.</li>
  <li><strong>Print Updated File:</strong> Read and printed the updated contents of the file to verify the changes.</li>
</ul>
