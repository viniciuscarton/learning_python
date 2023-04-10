# Learning Python
'Learning Python' is a Django made repository for my Python mini projects. It stores Python scripts (.py) in an arcade-like interface and allows the user to download them. These scripts are divided by level (basic, intermediate, advanced) and purpose (utility, fun).  

    ❗ Before running Learning Python, set a SECRET_KEY in settings.py ❗

## Content
The app has three pages. The first one allows the user to select a level (basic, intermediate or advanced). The second one allows the user to select the purpose of the script (fun or utility). The third and last page is rendered accordingly to the previous two. It displays the scripts in animated, pulsating icons. Below the icons, there is the name of the script and a download button. If the user puts the cursor on top of the pulsating icons, a brief description of the script will appear at the bottom of the page. If the user clicks on the Python spinning logo at the top of the page, he or she will be directed to the index, first page. 

![Interface](learningpython.gif)

## How to use it
The three templates (index, file and level) are not to be altered. When wanting to add a new script, here are the steps the user should take:

1. Add the script to the static/script/ folder;
2. Add a (preferably square) image (with the same name as the script, but without the extension) to the static/image/ folder to represent the script (this step is optional);
3. In the views.py, add the path to the script in script_dict according to its classification which is up to the user (basic/intermediate/advanced, fun/utility);
4. In the views.py, add an entry to the 'descriptions' dictionary in the two file_view's functions. This entry should follow the pattern: 'script_name (without the extension): script_description'.

With those steps, the app will be able to properly display the script according to its classification.

## Attention ❗
The functionality of this app is dependent on the right naming of the files (script, image, view.py entries and paths). The naming pattern is up to to user, but it is recommended that it avoid spaces, numbers, punctuation marks and symbols. So: <br>
✔️ colorofcars.py <br>
✔️ whichdayisit.py <br>
✔️ oneormoreapples.py <br>
❌ color-of-cars?.py <br>
❌ which day is it.py <br>
❌ 1ormoreapples.py <br>


