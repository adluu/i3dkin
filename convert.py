import cv2
import math
import scipy.misc
import os, sys

data_root='/users/becky/documents/cmpe295/UCF_Crimes'
videos_root =os.path.join(data_root,'Videos')
images_root=os.path.join(data_root,'images')

def make_list(split):
    start=True
    with open('/users/becky/documents/cmpe295/i3dkin/list/ucfcrime_list/train.list', "w") as f:
        sp=open(os.path.join(data_root,'Action_Regnition_splits','train_00%d.txt'%split))
        labels=open(os.path.join(data_root,'Action_Regnition_splits','ClassIDs.txt'))
        labarr=[]
        for line in labels:
            labarr.append(line.split(' ')[0])
        for line in sp:
            file_dir=line.strip('\n').strip(' ')
            labind=(labarr.index(line.strip('\n').strip(' ').split('/')[0]))

            if not start:
                f.write("\n")
            else:
                start=False
            f.write(os.path.join(images_root,file_dir[:-4])+" %d"%labind)
        f.close()
        start=True
    with open('/users/becky/documents/cmpe295/i3dkin/list/ucfcrime_list/test.list', "w") as f:
        sp=open(os.path.join(data_root,'Action_Regnition_splits','test_00%d.txt'%split))
        labels=open(os.path.join(data_root,'Action_Regnition_splits','ClassIDs.txt'))
        labarr=[]
        for line in labels:
            labarr.append(line.split(' ')[0])
        for line in sp:
            file_dir=line.strip('\n').strip(' ')
            labind=(labarr.index(line.strip('\n').strip(' ').split('/')[0]))

            if not start:
                f.write("\n")
            else:
                start=False
            f.write(os.path.join(images_root,file_dir[:-4])+" %d"%labind)
        f.close()



def extract_splits(split):
    trfile=open(os.path.join(data_root,'Action_Regnition_splits','train_00%d.txt'%split))
    for line in trfile.readlines():
        
        file_dir=line.strip('\n').strip(' ')
 
        videoFile = os.path.join(videos_root,file_dir)
        if not os.path.exists(os.path.join(images_root,file_dir[:-4],'i')):
            os.makedirs(os.path.join(images_root,file_dir[:-4],'i'))
        if not os.path.exists(os.path.join(images_root,file_dir[:-4],'x')):
            os.makedirs(os.path.join(images_root,file_dir[:-4],'x'))
        if not os.path.exists(os.path.join(images_root,file_dir[:-4],'y')):
            os.makedirs(os.path.join(images_root,file_dir[:-4],'y'))
    
        if os.listdir(os.path.join(images_root,file_dir[:-4],'i'))==[]:
            
            cap1 = cv2.VideoCapture(videoFile)
            
            num=0
            cap1.set(5,20)
            fps = cap1.get(5)
            print("extracting ", file_dir)
            while(cap1.isOpened()):
                frameId = cap1.get(1) #current frame number
                ret, frame = cap1.read()
                if (ret != True):
                    break
                if (frameId % math.floor(fps) == 0):
                    save_img=os.path.join(images_root,file_dir[:-4],'i','%d.jpg'%num)
                    num+=1
                    scipy.misc.imsave(save_img,frame)
            #filename ="test%d.jpg" % count;count+=1
            #cv2.imwrite(filename, frame)
            cap1.release()
                
    tefile=open(os.path.join(data_root,'Action_Regnition_splits','test_00%d.txt'%split))
    for line in tefile.readlines():
        file_dir=line.strip('\n').strip(' ')
        videoFile = os.path.join(videos_root,file_dir)
        if not os.path.exists(os.path.join(images_root,file_dir[:-4],'i')):
            os.makedirs(os.path.join(images_root,file_dir[:-4],'i'))
        if not os.path.exists(os.path.join(images_root,file_dir[:-4],'x')):
            os.makedirs(os.path.join(images_root,file_dir[:-4],'x'))
        if not os.path.exists(os.path.join(images_root,file_dir[:-4],'y')):
            os.makedirs(os.path.join(images_root,file_dir[:-4],'y'))
            
        if os.listdir(os.path.join(images_root,file_dir[:-4],'i'))==[]:
                
            cap2 = cv2.VideoCapture(videoFile)
                
            num=0
            cap2.set(5,20)
            fps = cap2.get(5)
            print("extracting ",file_dir)
            while(cap2.isOpened()):
                frameId = cap2.get(1) #current frame number
                ret, frame = cap2.read()
                if (ret != True):
                    break
                if (frameId % math.floor(fps) == 0):
                    save_img=os.path.join(images_root,file_dir[:-4],'i','%d.jpg'%num)
                    num+=1
                    scipy.misc.imsave(save_img,frame)
                    #filename ="test%d.jpg" % count;count+=1
                    #cv2.imwrite(filename, frame)

            cap2.release()
    
def extract_all():
    for cls_names in os.listdir(videos_root):
        cls_path=os.path.join(videos_root,cls_names)
        for video_ in os.listdir(cls_path):
            count = 0
            file_dir = os.path.join(cls_names,video_) #in format of Label/Vidname_x264.mp4
            videoFile = os.path.join(videos_root,file_dir)
            if not os.path.exists(os.path.join(images_root,file_dir[:-4],'i')):
                os.makedirs(os.path.join(images_root,file_dir[:-4],'i'))
            if not os.path.exists(os.path.join(images_root,file_dir[:-4],'x')):
                os.makedirs(os.path.join(images_root,file_dir[:-4],'x'))
            if not os.path.exists(os.path.join(images_root,file_dir[:-4],'y')):
                    os.makedirs(os.path.join(images_root,file_dir[:-4],'y'))

            if os.listdir(os.path.join(images_root,file_dir[:-4],'i'))==[]:

                cap = cv2.VideoCapture(videoFile)

                num=0
                cap.set(5,20)
                fps = cap.get(5)
                print("extracting ",file_dir)
                while(cap.isOpened()):
                    frameId = cap.get(1) #current frame number
                    ret, frame = cap.read()
                    if (ret != True):
                        break
                    if (frameId % math.floor(fps) == 0):
                        save_img=os.path.join(images_root,file_dir[:-4],'i','%d.jpg'%num)
                        num+=1
                        scipy.misc.imsave(save_img,frame)
                        #filename ="test%d.jpg" % count;count+=1
                        #cv2.imwrite(filename, frame)

                cap.release()



'''def get_video_list():
    video_list=[]
    for cls_names in os.listdir(videos_root):
        cls_path=os.path.join(videos_root,cls_names)
        for video_ in os.listdir(cls_path):
            video_list.append(video_)
    video_list.sort()
    return video_list,len(video_list)'''

extract_splits(split)
make_list(split)
#extract_all()
#vl, l=get_video_list()
#print("vl= ",vl)
#print("len= ",l)




