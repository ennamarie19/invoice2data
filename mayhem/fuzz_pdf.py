#!/usr/bin/env python3

import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports(include=["invoice2data"]):
    from invoice2data import extract_data

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        with fdp.ConsumeTemporaryFile('.pdf', all_data=True, as_bytes=False) as f:
            extract_data(f, templates=None, input_module=None)
    except OSError:
        return -1

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
