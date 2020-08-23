# Password Generator

Set "generate-password" as Executable like `chmod +x ./generate-password` - Now you can use the Command in the Dir.


```
generate-password 16 3 True True True $!=
```


Generate the Following: 
```
fa\"Tu2yR3kts*^z5TKY
TQKome>EHpz:=VxcF!0}
3}On5g,^}HOWtw~+H91g
```

## Arguments:

| Name        | Description                 | Type Value | Default |
|-------------|-----------------------------|------------|---------|
| length      | Length of Password          | Int        | 16      |
| num         | How Many Password Generated | Int        | 3       |
| punctuation | Punctuation (Special Chars) | Bool       | True    |
| digits      | Digits                      | Bool       | True    |
| letters     | Letters                     | Bool       | True    |
| excludes    | Special Chars Exclude       | String     | None    |