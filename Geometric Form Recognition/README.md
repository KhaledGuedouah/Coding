# Geometric Form Recognition

This project recognizes simple geometric forms using geometric moments and Legendre moments extracted from BMP images. It compares the input image to a small database of reference images using Euclidean distance, then optionally reconstructs the closest match.

**Features**
1. Build a moments database from reference BMPs.
2. Recognize the closest shape from a test image.
3. Reconstruct an image from stored moments.

**Repository Layout**
1. `DATA/DB/` reference BMPs and generated moment files.
2. `InputImg/` test images and the list in `InputImg/TestImg.txt`.
3. `main.c` interactive CLI entry point.

**Build**
Use any C compiler. With GCC/MinGW:

```bash
gcc -O2 -Wall -Wextra -o geom_recognition \
  main.c tools.c myBmpGris.c moment_geometrique.c legendre.c \
  listeSC.c constructeurBDD.c img_reconstruct.c -lm
```

**Run**
```bash
./geom_recognition
```

You will be prompted to:
1. Rebuild the moments database (optional).
2. Pick an input image from `InputImg/`.
3. Reconstruct the closest match (optional).

The reconstruction is saved to `ImgRec.bmp`.

**Notes**
1. Inputs are expected to be 24-bit BMPs (the reader uses a single channel).
2. The database list is defined in `DATA/DB/DBimg.txt`.
