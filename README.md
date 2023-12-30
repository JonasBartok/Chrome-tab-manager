
# CHROME TAB MANAGER +

This is CHROME TAB MANAGER + a simple but powerful tool to enhance your browsing experience in Google Chrome. 
This program is used to save open chrome tabs for later use in a .txt file.

## Video Demo 

https://youtu.be/9FiHPOmFEf8

 



## Documentation

To store URLs from opened Chrome tabs run:

```bash
  python project.py --store file_name.txt
```

To store URLs from opened Chrome tabs to a .txt file with current date as a name in format YYYY-MM-DD run: 

```bash
  python project.py --store currently
```

To load the Chrome tabs from file:

```bash
  python project.py --load file_name.txt
```
#### Things to keep in mind: 
If two or more tabs with the same URL are open side by side, the program will malfunction. 

If no Chrome tab is open, the --store argument will exit with the error message "An error occurred. Is Chrome opened?"

## What does each function do? 

### main 
The "main" function is used to create argsparse arguments and to execute other functions based on system input.

### get_urls
The "get_urls" function is used to get the URLs of open tabs in Google Chrome and return them as a list.

### load_urls 
The "load_urls" function is used to retrieve URLs from a .txt file and open them in your preferred browser (I recommend Chrome).

### store_urls
The "store_urls" function takes one argument, which is a list of URLs to be stored in a .txt file. The list comes from the return value of the "get_urls" function.

### focus_chrome_tab
The "focus_chrome_tab" function is used to focus/activate the Chrome window. The "get_urls" function can then collect URLs without the user having to manually switch to the Chrome window.
## How to install 

Clone the project

```bash
  git clone https://github.com/code50/135703747.git
```

Install dependencies

```bash
  pip install -r requirements
```

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to enhance the project.



## License

[MIT](https://choosealicense.com/licenses/mit/)


## 🔗 Links


[![instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://twitter.com/)

