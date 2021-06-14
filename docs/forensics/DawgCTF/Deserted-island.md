## Deserted Island Toolkit 
##### Challenge Descritpion:
What would a drunken sailor do? (Wrap the output in DawgCTF{ })
[Challenge file](https://drive.google.com/file/d/1vYUIAPIeQgE6x781tH6SU3uU0YSx5Yxv/view?usp=sharing)
- On analysing the given zip file we find a ``.cdda`` file.
- On opening that file in audacity and viewing it in spectrogram, we find a morse code:

```... ----- ... .. ... -. --- - - .... . .- -. ..... .-- ...-- .-.```
- And decoding it gives the flag 
```
DawgCTF{S0SISNOTTHEAN5W3R}
```
