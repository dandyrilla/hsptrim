#!/usr/bin/env python3

import argparse


__version__ = '2.0.0'


def trim_se(args):
    print(args)


def trim_pe(args):
    print(args)


def add_common_arguments(parser):

    parser.add_argument('-t', type=str, default='sanger', metavar='STR',
                        help='Type of quality values: illumina(+64), sanger(+33), phred(+0) [sanger]')
    parser.add_argument('-d', type=str, default='3p', metavar='STR',
                        help='End to be trimmed: both, 5p, 3p [3p]')
    parser.add_argument('-q', type=int, default=30, metavar='INT',
                        help='Minimum quality to get reward score [30]')
    parser.add_argument('-l', type=int, default=20, metavar='INT',
                        help='Threshold to keep a read based on length after trimming [20]')
    parser.add_argument('-w', type=int, default=1, metavar='INT',
                        help='Reward score [1]')
    parser.add_argument('-e', type=int, default=-5, metavar='INT',
                        help='Panelty score [-5]')


def main():

    parser = argparse.ArgumentParser(
        description='A script to trim FASTQ reads using the highest scoring path algorithm.'
    )
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')

    subparsers = parser.add_subparsers(dest='command')

    parser1 = subparsers.add_parser('se', help='trim single-end reads')
    parser1.set_defaults(func=trim_se)
    add_common_arguments(parser1)
    parser1.add_argument('in_fq', type=str, help='Input single-end FASTQ file')
    parser1.add_argument('out_fq', type=str, help='Output single-end FASTQ file')

    parser2 = subparsers.add_parser('pe', help='trim paired-end reads')
    parser2.set_defaults(func=trim_pe)
    add_common_arguments(parser2)
    parser2.add_argument('in1_fq', type=str, help='Input paired-end FASTQ file 1')
    parser2.add_argument('in2_fq', type=str, help='Input paired-end FASTQ file 2')
    parser2.add_argument('out1_fq', type=str, help='Output trimmed FASTQ file 1')
    parser2.add_argument('out2_fq', type=str, help='Output trimmed FASTQ file 2')
    parser2.add_argument('out3_fq', type=str, help='Output trimmed singles FASTQ file')

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
