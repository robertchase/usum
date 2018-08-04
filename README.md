# usum

cli tool for summing columns in a text file


### introduction

In the spirit of small and focused command-line programs that comprise
the (*)nix shell,
`usum` provides a simple way to sum columns in text data.

### example

Here is some test data:

```
home/test:~> cat data
Jul 30 11
Jul 31 97
Jul 31 8
Aug 1 127
Aug 2 17
Aug 2 54
```

Sum the first two columns (think of the `SQL groupby` functionality):

```
home/test:~> cat data | usum 1 2
Aug 1 127
Aug 2 71
Jul 30 11
Jul 31 105
```

Specified order of the columns is preserved:

```
home/test:~> cat data | usum 2 1
31 Jul 105
1 Aug 127
30 Jul 11
2 Aug 71
```

Sum just one column, with dubious meaning:

```
home/test:~> cat data | usum 1
Aug 5 198
Jul 92 116
```

Combine with
[ucol](https://github.com/robertchase/ucol):
```
home/test:~> cat data | ucol 1 3
Jul 11
Jul 97
Jul 8
Aug 127
Aug 17
Aug 54

home/test:~> cat data | ucol 1 3 | usum 1
Aug 198
Jul 116
```

### syntax
```
usum [-h] [groupby [groupby ...]]
```

### options
```
```
