# Filters

**Description**: No bypass!<br>
**Author:  [Av4nth1ka](https://twitter.com/av4nth1ka)**

**Solution**: 

In this challenge, we have a few restricted characters: single quotes ('), double quotes ("), backticks (), dots (.), dollar signs ($), or forward slashes (/) and restricted functions require, include.<br>
<br>
Payload: `http://localhost:8080/?command=highlight_file(glob(%22fl*txt%22)[0]);`<br>
<br>
The payload uses the highlight_file()function in combination with theglob()function to find the file with a name starting with "fl" and ending with "txt". Theglob()function returns an array of matching file paths. By using `glob("fl*txt")[0]`, we get the first matching file path, which is then passed to the highlight_file()` function.<br>


Flag: `shaktictf{y0u_byp4553d_7h3_f1l73r5_y4y}`              