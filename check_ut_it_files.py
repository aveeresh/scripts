import os
import sys

MCAL_MODULE_LIST      = "Can Fls Spi"
COM_STACK_MODULE_LIST = "CanIf PduR Com CanSM CanNm CanTp CanTrcv"
MEM_STACK_MODULE_LIST = "NvM MemIf Fee"  
SYS_STACK_MODULE_LIST = "Tm FiM EcuM"

#Code starts here
dir = os.getcwd() + '/build'

mcal_split = MCAL_MODULE_LIST.split()
comstack_split = COM_STACK_MODULE_LIST.split()
memstack_split = MEM_STACK_MODULE_LIST.split()
systemstack_split = SYS_STACK_MODULE_LIST.split()

elf_files = []

for path, subdirs, files in os.walk(dir):
	for file in files:
		elf_files.append(file)

all_modules = mcal_split + comstack_split + memstack_split + systemstack_split

# print( elf_files )
# print( all_modules )

missing_files = []

for mod in all_modules:
	#print( 'Module - ' + mod )
	ut_flag = 0
	it_flag = 0
	for file in elf_files:
		#print( 'File - ' + file )
		if( file.find('_'+mod+'_')>0 ):
			#print( '%s found' % (mod) )
			if( (file.find('UT')>0) and ut_flag==0 ):
				ut_flag = 1
				#print( 'UT elf found' )
			elif( (file.find('IT')>0) and it_flag==0 ):
				it_flag = 1
				#print( 'IT elf found' )
				
	#print( 'ut_flag = ' + str(ut_flag) + ' it_flag = ' + str(it_flag) )
	if( (ut_flag==0) or (it_flag==0) ):
		if( ut_flag==0 ):
			missing_files.append('UBSW_'+mod+"_UT_SAMC21J18A.elf")
		if( it_flag==0 ):
			missing_files.append('UBSW_'+mod+"_IT_SAMC21J18A.elf")
		#print( file + ' added to empty list' )

if( len(missing_files) != 0 ):
	print( "Following files are missing" )

	for file in missing_files:
		print( file )
else:
	print( "All UT and IT files present for all modules" )