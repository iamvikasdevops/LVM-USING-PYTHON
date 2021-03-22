import os

def lvm(client_input):
    if client_input=="1":
        os.system('fdisk -l')
        print()
        dis=input("Enter device or disk name: ")
        os.system("pvcreate {}".format(dis))
        os.system('pvdisplay')
        print()
        vg_name=input("Enter Volume group name and pv seprated by space: ")
        os.system('vgcreate {}'.format(vg_name))
        print()
        print("Now, Have to create LV")
        print()
        lv_name=input("Enter LV NAME: ")
        lv_size=input("Enter LV Size: ")
        os.system('vgdisplay')
        print()
        vg_sel=input("Select one of the VG from Above Given VGs for creating LV")
        os.system('lvcreate -n {0} -L {1} {2}'.format(lv_name,lv_size,vg_sel))
        print("\n ")
        os.system('lvdisplay {}/{}'.format(vg_sel, lv_name))
        print("\n")
        os.system('mkfs.ext4 /dev/{}/{}'.format(vg_sel, lv_name))
        print("\n")
        fol_name=input("Enter Folder name")
        os.system('mkdir {}'.format(fol_name))
        os.system('mount /dev/{}/{} {}'.format(vg_sel, lv_name, fol_name))
        print()
        print("See Whether LVM mounted or not")
        print("\n")
        os.system('df -h')
    elif client_input=="2":
        ext_size=input("Enter the Size that you want to extend in LV:")
        print("\n")
        os.system('lvdisplay')
        print()
        lvname=input("Enter the name of the LogicalVolume(LV):")
        print("\n")
        os.system('lvextend --size +{0} {1}'.format(ext_size, lvname))
        os.system('resize2fs {}'.format(lvname))
    elif client_input=="4":
        os.system('pvs')
        pv_exte=input("enter pv name in format like /dev/diskname as /dev/sdd: ")
        os.system('vgs')
        vg_name=input("enter Vg name for extending its capacity:")
        os.system('vgextend {} {}'.format(vg_name, pv_exte))
    elif client_input=="5":
        print(" here is a list of All created PVs")
        os.system('pvs')
    elif client_input=="6":
        print("Here is a list of All created VGs")
        os.system('vgs')
    elif client_input=="3":
        hts=input("Do you really want to reduce the size of LVs (yes/no):")
        if hts=="yes":
            os.system('lvscan')
            lv=input("Enter LV Name From above given list:")
            os.system('umount -v {}'.format(lv))
            print()
            os.system('e2fsck -ff {}'.format(lv))
            print()
            size_r=input("how much you want to kept your LV Size")
            os.system('resize2fs {} {}'.format(lv, size_r))
            print()
            os.system('lvreduce {} {}'.format(size_r, lv))
            print()
            dr=input('Enter Directory Name')
            os.system('mount {} {}'.format(lv, dr))
            print("Check the Size of Your Mounted Folder or Directory")
            os.system('df -h | grep {}'.format(lv))
    else:
        os.system('exit')


while True:
    os.system('tput setaf 5')
    print(" \t\t\t\t\t\t-----------------------------------------------------------------------")
    os.system('tput bold')
    print(" \t\t\t\t\t\t_________________________ LVM AUTOMATION USING PYTHON _________________")
    os.system('tput setaf 5')
    os.system(' tput setaf 7')
    os.system('tput setaf 4')
    client_input=input (""" 
           Press:1:For Creating LV(Logical Volume) and Mounting it to the folder so that you can use it 
           Press:2:For Extending the Logical Volume
           Press:3:For Reducing LV(Logical Volume) 
           Press:4:For Adding more PVs to VolumeGroup(VG) or extending VG
           Press:5:For Checking all created PVs
           Press:6:For Checking or Viewing all created VGs
           Press:7:For Checking All LV Mountpath
           Press:8:For closing LVM Automation Program  
                     """)
    os.system('tput setaf 7')
    
    if client_input=="8":
        break
    elif client_input=="0":
        print("Sorry , You have provided wrong input")
    else:
        lvm(client_input)

    

