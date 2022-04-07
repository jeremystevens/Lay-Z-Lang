python compiler.py --filename code.lzy --output output.ll
llc -filetype=obj output.ll -o output.o
gcc output.o -o output
chmod +x output
./output
