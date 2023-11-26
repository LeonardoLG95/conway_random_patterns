import sys
from rplife import patterns, views
from rplife.cli import get_command_line_args


def main():
    args = get_command_line_args()

    View = getattr(views, args.view)

    if args.all:
        for pattern in patterns.get_all_patterns():
            _show_pattern(View, pattern, args)

    elif args.pattern in [pat.name for pat in patterns.get_all_patterns()]:
        _show_pattern(View, patterns.get_pattern(name=args.pattern), args)

    else:
        # My addition:
        pattern = patterns.generate_pattern(args.pattern)
        _show_pattern(View, pattern, args)


def _show_pattern(View, pattern, args):
    try:
        View(pattern=pattern, gen=args.gen, frame_rate=args.fps).show()
    except Exception as error:
        print(error, file=sys.stderr)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Thanks for playing!")
