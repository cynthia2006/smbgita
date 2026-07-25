>  “Yada yada hi dharmasya glanirbhavati bharata \
>  Abhyutthanam adharmasya tadatmanam srijamyaham \
> Paritranaya sadhunam vinashayacha dushktitam \
> Dharmasangsthapanarthaya samvabami yuge yuge” — Krishna, Srimadbhagvatgita 4:3

Srimadbhagvatgita's shlokas are scraped from https://shlokam.org/bhagavad-gita/index/. The original [Devnagari](https://en.wikipedia.org/wiki/Devanagari) script, and [IAST](https://en.wikipedia.org/wiki/International_Alphabet_of_Sanskrit_Transliteration) are preserved along with its meaning. The `data` folder is structured such that directories represent chapters with verses as consolidated into JSON files.

A Go module is provided for randomly sampling a shloka, displaying it to standard output. Here's how to use it:

```
$ git clone https://github.com/cynthia2006/smbgita
$ cd smbgita
$ go run . | cowsay
 _________________________________________
/ ātmaupamyena sarvatra samaṃ paśyati    \
| yo’rjuna sukhaṃ vā yadi vā              |
| duḥkhaṃ sa yogī paramo mataḥ            |
| 6-32                                    |
|                                         |
| He who, through the likeness (sameness) |
| of the Self, O Arjuna, sees equality    |
| everywhere, be it pleasure or pain, he  |
\ is regarded as the highest YOGI.        /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
$ 

```

Note that, the `data` folder must be placed adjacent to the Go executable. In future, `~/.local/share/gita` (user) or `/usr/share/gita` (system) paths will be considered as well.

 