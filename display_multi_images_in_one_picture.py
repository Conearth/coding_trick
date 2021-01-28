def matplotlib_multi_pic(img_list):
# items in img_list are objects of cv2.imread(...) 
    for i in range(8):
        img = img_list[i]
        print(img.shape)
        title="title"+str(i)
        #行，列，索引
        plt.subplot(3,3,i+1)
        plt.imshow(img)
        plt.title(title,fontsize=8)
        plt.xticks([])
        plt.yticks([])
    plt.show()
