from image import Image
def blur(unbluredImage):
    blurredImage = unbluredImage.copy()
    for row in range(1, unbluredImage.height - 1):
        for col in range(1, unbluredImage.width - 1):
            total = 0
            for yoffest in range(-1,2):
                for xoffset in range(-1,2):
                    total += unbluredImage.get(row+yoffest,col+xoffset)
            average = int(total / 9)
            blurredImage.set(row,col,average)
    return blurredImage