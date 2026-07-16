from distutils.core import setup, Extension

def main():
    print("RUNNING MAIN")
    setup(name="string_processing",
          version="1.0.0",
          description="Python interface for the fputs C library function",
          author="<etran13>",
          author_email="your_email@gmail.com",
          ext_modules=[Extension("string_processing", ["string_processing.c"])])

if __name__ == "__main__":
    main()