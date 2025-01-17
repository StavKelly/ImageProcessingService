from pathlib import Path
from matplotlib.image import imread, imsave

import matplotlib.pyplot as plt

def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


class Img:

    def __init__(self, path):
        """
        Do not change the constructor implementation
        """
        self.path = Path(path)
        self.data = rgb2gray(imread(path)).tolist()

    def save_img(self):
        """
        Do not change the below implementation
        """
        new_path = self.path.with_name(self.path.stem + '_filtered' + self.path.suffix)
        imsave(new_path, self.data, cmap='gray')
        return new_path


    def blur(self, blur_level=16):

        height = len(self.data)
        width = len(self.data[0])
        filter_sum = blur_level ** 2

        result = []
        for i in range(height - blur_level + 1):
            row_result = []
            for j in range(width - blur_level + 1):
                sub_matrix = [row[j:j + blur_level] for row in self.data[i:i + blur_level]]
                average = sum(sum(sub_row) for sub_row in sub_matrix) // filter_sum
                row_result.append(average)
            result.append(row_result)

        self.data = result

    def contour(self):
        for i, row in enumerate(self.data):
            res = []
            for j in range(1, len(row)):
                res.append(abs(row[j-1] - row[j]))

            self.data[i] = res

    def rotate(self):
        # Rotate the data by 180 degrees
        self.data = [row[::-1] for row in self.data[::-1]]

    def salt_n_pepper(self):
        # TODO remove the `raise` below, and write your implementation
        raise NotImplementedError()

    def concat(self, other_img, direction='horizontal'):
        # TODO remove the `raise` below, and write your implementation
        raise NotImplementedError()

    def segment(self):
        # TODO remove the `raise` below, and write your implementation
        raise NotImplementedError()

# Creating an instance of the Img class
my_img = Img('/Users/stavk/PycharmProjects/ImageProcessingService/polybot/test/beatles.jpeg')
print(my_img.path)
#print(my_img.data)

# Applying the rotate filter for 180
my_img.rotate()

# Save the modified image
saved_path = my_img.save_img()
print("Modified image saved to:", saved_path)

