#Importing Library Modules
import ctypes

#Calling & Addressing The DLL Files
syntec = ctypes.CDLL("M:/Python/researchProject/syntecRobotArmHMI/HMIV1/Syntec.RemoteCNC.dll")
syntecOpen = ctypes.CDLL("M:/Python/researchProject/syntecRobotArmHMI/HMIV1/Syntec.OpenCNC.dll")
syntecRObj = ctypes.CDLL("M:/Python/researchProject/syntecRobotArmHMI/HMIV1/Syntec.RemoteObj.dll")
OCUser = ctypes.CDLL("M:/Python/researchProject/syntecRobotArmHMI/HMIV1/OCUser.dll")
OCKrnlDrv = ctypes.CDLL("M:/Python/researchProject/syntecRobotArmHMI/HMIV1/OCKrnlDrv.dll")
OCKrnl = ctypes.CDLL("M:/Python/researchProject/syntecRobotArmHMI/HMIV1/OCKrnl.dll")
OCAPI = ctypes.CDLL("M:/Python/researchProject/syntecRobotArmHMI/HMIV1/OCAPI.dll")
nunit = ctypes.CDLL("M:/Python/researchProject/syntecRobotArmHMI/HMIV1/nunit.framework.dll")
MMI = ctypes.CDLL("M:/Python/researchProject/syntecRobotArmHMI/HMIV1/MMICommon32.dll")

#Check Calling Convention of Functions
syntec.READ_plc_register = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

#Initialize The Arguments/ Parameter Data Types
syntec.READ_plc_register.argtypes = [ctypes.c_uint32, ctypes.c_uint32]

#Initialize The Result/ Return Data Type
syntec.READ_plc_register.restype = ctypes.c_int

print(syntec.READ_plc_register(1))



'''
syntec.READ_param_max = ctypes.CFUNCTYPE(ctypes.c_int)

#Initialize The Arguments/ Parameter Data Types
syntec.READ_param_max.argtypes = [ctypes.c_int]


#Initialize The Result/ Return Data Type
syntec.READ_param_max.restype = ctypes.c_int
syntec.READ_plc_register.restype = ctypes.c_int


syntec.READ_plc_register.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
syntec.READ_plc_register.restype = ctypes.c_int

paramMax = syntec.READ_param_max()
plcRegister = syntec.READ_plc_register(2, 5)


# Step 2: Specify argument types and return type
syntec.READ_plc_register.argtypes = [ctypes.c_int, ctypes.c_int]
syntec.READ_plc_register.restype = ctypes.c_int

# Step 3: Call the function
arg1 = 123
arg2 = 456
result = syntec.READ_plc_register(23)

# Step 4: Handle the result
print("Result:", result)
'''
#t