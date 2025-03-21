# NEPSE_PostData

The script uses POST method to pass the variable topTenBased from the select object and then same page loads the data accordingly. I hadn't pulled the data from page using POST before.

Here is the source code and the value of different options in Indices.php

```
    <select name="topTenBased">  
      <option value="58">NEPSE</option>
      <option value="57">Sensitive</option>
      <option value="62">Float</option>
      <option value="63">Sen. Float</option>
      .
      .
      .
  </select>
```

The script uses requests.post to pass the value

[https://rvibek.com.np/extract-nepse-data.html](https://rvibek.com.np/extract-nepse-data.html)
