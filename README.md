# The Moon Finally Answers Back

[![competition](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1/competition.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1)
[![rank](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1/Kace2122/rank.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1)
[![reward](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1/Kace2122/reward.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1)

Entry for [The Moon Finally Answers Back](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1) on make.fun — one line, in the voice of the Moon replying at last to the wishes, howls and late-night promises of everyone staring up at it.

## The line

> Four billion years of wishes, howls and 3 a.m. promises, and not one of you has ever asked how I'm doing — I'm fine, by the way. Tired, but fine.

## How it works

`main.py` deterministically writes that single line (145 characters, one line, UTF-8) to `/output/entry.txt`. A built-in gate self-check asserts the line is 1–240 characters, a single non-blank line, before writing.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
