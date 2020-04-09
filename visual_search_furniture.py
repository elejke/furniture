
# coding: utf-8

# In[1]:


# !pip install --upgrade google-cloud-vision


# In[5]:


import os
import glob
#import numpy as np
#import pandas as pd

#from PIL import Image

from google.cloud import vision

#from matplotlib import pylab as plt
#from tqdm import tqdm_notebook as tqdm
#
#
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/root/shared/old/vs/gig-canon-cv-87b570dfc608.json'
#
# PROJECT_ID = 'gig-canon-cv'
# LOCATION = 'us-west1'
#
# PRODUCT_SET_ID = 'test_furniture'
# PRODUCT_SET_DISPLAY_NAME = 'test_furniture_display_name'
#
# TEST_IMAGE_ROOT = "/mnt/datasets/raw/"
#
# PRODUCT_CATEGORY = "homegoods-v2"
#
# TEST_IMAGE_ROOT = "/mnt/datasets/raw/furniture/"
#
# #test_image_list = glob.glob(os.path.join(TEST_IMAGE_ROOT + "*.jpg"))
# #len(test_image_list)
#
# def get_similar_products_file(
#         project_id, location, product_set_id, product_category,
#         file_path, filter):
#     """Search similar products to image.
#     Args:
#         project_id: Id of the project.
#         location: A compute region name.
#         product_set_id: Id of the product set.
#         product_category: Category of the product.
#         file_path: Local file path of the image to be searched.
#         filter: Condition to be applied on the labels.
#         Example for filter: (color = red OR color = blue) AND style = kids
#         It will search on all products with the following labels:
#         color:red AND style:kids
#         color:blue AND style:kids
#     """
#     # product_search_client is needed only for its helper methods.
#     product_search_client = vision.ProductSearchClient()
#     image_annotator_client = vision.ImageAnnotatorClient()
#
#     # Read the image as a stream of bytes.
#     with open(file_path, 'rb') as image_file:
#         content = image_file.read()
#
#     # Create annotate image request along with product search feature.
#     image = vision.types.Image(content=content)
#
#     # product search specific parameters
#     product_set_path = product_search_client.product_set_path(
#         project=project_id, location=location,
#         product_set=product_set_id)
#     product_search_params = vision.types.ProductSearchParams(
#         product_set=product_set_path,
#         product_categories=[product_category],
#         filter=filter)
#     image_context = vision.types.ImageContext(
#         product_search_params=product_search_params)
#
#     # Search products similar to the image.
#     response = image_annotator_client.product_search(
#         image, image_context=image_context)
#
#     index_time = response.product_search_results.index_time
#
#     results = response.product_search_results.results
#
#     return results
#
# #IMAGE_ROOT = "/mnt/datasets/raw/furniture/"
#
# def get_similar(img_path, df_paintings=df_paintings):
#     similar_products = get_similar_products_file(PROJECT_ID, LOCATION, PRODUCT_SET_ID,
#                                                  PRODUCT_CATEGORY, img_path, '')
#
#     fig, axes = plt.subplots(3, 3, figsize=[10, 10])
#
#     for i, product_ in enumerate(similar_products[:9]):
#         name_ = product_.image.split("/")[-1] + ".jpg"
#         product_ = product_.product
#
#         axes[i // 3, i % 3].imshow(plt.imread(os.path.join(IMAGE_ROOT, name_)))
#         axes[i // 3, i % 3].axis('off')
#         filename_ = product_.name.split('/')[-1].replace('!', "")
#     plt.savefig("temp__.jpg")
#     plt.close()
#     neigh_img = plt.imread("temp__.jpg")
#     plt.close()
#     return neigh_img
#
# plt.imshow(plt.imread(FILE_PATH))
#
# img = get_similar(FILE_PATH)
# plt.figure(figsize=[11, 11])
# plt.imshow(img)
#
#
# import os
# import io
# import base64
# import skimage
# import requests
# import threading
#
# import telebot
#
#
# # In[104]:
#
#
# from skimage import io
#
#
# # In[105]:
#
#
# token = "810723384:AAFzLFXPEmtcPM4v_l3DvTzaWVYr3f9J1_8"
#
#
# # In[106]:
#
#
# bot = telebot.TeleBot(token)
#
#
# # In[107]:
#
#
# @bot.message_handler(commands=["start"])
# def send_welcome(message):
#     bot.reply_to(message, "Hello there")
#
# @bot.message_handler(func=lambda message: True, content_types=["document"])
# def echo_document(message):
#     URL_ROOT = "https://api.telegram.org/file/bot"
#     IMG_PATH = "temp_img.jpg"
#     try:
#         file_path = bot.get_file(message.document.file_id).file_path
#         file_url = os.path.join(URL_ROOT + token, file_path)
#
#         img = io.imread(file_url)
#         plt.imsave(IMG_PATH, img)
#         img_neigh = get_similar(IMG_PATH)
#         plt.imsave(IMG_PATH, img_neigh)
#         plt.close()
#         img_neigh = open(IMG_PATH, 'rb')
#         bot.send_photo(message.chat.id,
#                        img_neigh,
#                        reply_to_message_id=message.message_id)
#     except:
#         bot.send_message(message.chat.id, "Internal error")
#
# @bot.message_handler(func=lambda message: True, content_types=["photo"])
# def echo_photo(message):
#     bot.send_message(message.chat.id, "Please send image as document")
#
# @bot.message_handler(func=lambda message: True)
# def echo_other(message):
#     bot.send_message(message.chat.id, "Only text and images are supported")
#
#
# bot.polling()

