#!/usr/bin/env python2
################################################################
#  This file part of GALA Gap-free Long-reads Assembler        #
#  Auther: Mohamed awad                                        #
#  Company: Xiangchao Gan lab (MPIPZ)                          #
#  Released under the (MIT) license (see LICENSE file)         #
################################################################

import os
import gzip
def read_extract(read_file,names_file,file_type='fa'):
    if read_file[-2:]=='gz':
        a=gzip.open(read_file)
    else:
        a=open(read_file)
    b=list(open(names_file))
    c=list(set(b))
    d={}
    for base in c:
        d[base.replace('\n','')]=''
    if file_type=='fa' or file_type=='fasta':
        a=list(a)
        a=''.join(a)
        a=a.split('>')[1:]
        for bo in a:
            key=bo.split('\n')[0].split(' ')[0].replace('>','')
            try:
                d[key]=bo.split('\n')[0].replace('>','@')+'\n'+''.join(bo.split('\n')[1:])+'+\n'+len(''.join(bo.split('\n')[1:]))*'B'+'\n'
            except:
                continue
    elif file_type=='fq'or file_type=='fastq':
        while True:
            line1 = a.readline()
            line2 = a.readline()
            line3 = a.readline()
            line4 = a.readline()
            key=line1.split(' ')[0].replace('@','').replace('\n','')
            try:
                d[key]=line1+line2+line3+line4
            except:
                continue
            if line1=='':
                break
    else:
        Print('Unknown File Type')
    g=open(names_file.replace('_names','.fq'),'w')
    for base in c:
        g.writelines(d[base.replace('\n','')])
    g.close()
