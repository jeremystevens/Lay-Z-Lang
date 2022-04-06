; ModuleID = "output.ll"
target triple = ""
target datalayout = ""

@"fmt_double" = constant [4 x i8] c"%lf\00"
@"fmt_string" = constant [3 x i8] c"%s\00"
@"fmt_int" = constant [3 x i8] c"%d\00"
@"fmt_newline" = constant [2 x i8] c"\0a\00"
declare i32 @"printf"(i8* %".1", ...) 

declare i8* @"malloc"(i32 %".1") 

declare void @"memcpy"(i8* %".1", i8* %".2", i32 %".3") 

declare i32 @"scanf"(i8* %".1", ...) 

declare void @"realloc"(i8* %".1", i32 %".2") 

define i32 @"main"() 
{
entry:
  %"x" = alloca i32
  store i32 33, i32* %"x"
  %"z" = alloca i32
  store i32 50, i32* %"z"
  %"x_val" = load i32, i32* %"x"
  %"z_val" = load i32, i32* %"z"
  %"t" = add i32 %"x_val", %"z_val"
  %"y" = alloca i32
  store i32 %"t", i32* %"y"
  %"x_val.1" = load i32, i32* %"x"
  %"y_val" = load i32, i32* %"y"
  %"t.1" = add i32 %"x_val.1", %"y_val"
  %"z_val.1" = load i32, i32* %"z"
  %"t.2" = add i32 %"t.1", %"z_val.1"
  %"p" = alloca i32
  store i32 %"t.2", i32* %"p"
  %"fmt_ptr" = getelementptr [3 x i8], [3 x i8]* @"fmt_int", i32 0, i32 0
  %"p_val" = load i32, i32* %"p"
  %"print" = call i32 (i8*, ...) @"printf"(i8* %"fmt_ptr", i32 %"p_val")
  %"fmt_ptr.1" = getelementptr [2 x i8], [2 x i8]* @"fmt_newline", i32 0, i32 0
  %"print.1" = call i32 (i8*, ...) @"printf"(i8* %"fmt_ptr.1")
  %"APPLE" = alloca i32
  store i32 1, i32* %"APPLE"
  %"BANANA" = alloca i32
  store i32 2, i32* %"BANANA"
  %"CANTALOUPE" = alloca i32
  store i32 3, i32* %"CANTALOUPE"
  %"fmt_ptr.2" = getelementptr [3 x i8], [3 x i8]* @"fmt_int", i32 0, i32 0
  %"CANTALOUPE_val" = load i32, i32* %"CANTALOUPE"
  %"print.2" = call i32 (i8*, ...) @"printf"(i8* %"fmt_ptr.2", i32 %"CANTALOUPE_val")
  %"fmt_ptr.3" = getelementptr [2 x i8], [2 x i8]* @"fmt_newline", i32 0, i32 0
  %"print.3" = call i32 (i8*, ...) @"printf"(i8* %"fmt_ptr.3")
  %"fmt_ptr.4" = getelementptr [3 x i8], [3 x i8]* @"fmt_int", i32 0, i32 0
  %"APPLE_val" = load i32, i32* %"APPLE"
  %"print.4" = call i32 (i8*, ...) @"printf"(i8* %"fmt_ptr.4", i32 %"APPLE_val")
  %"fmt_ptr.5" = getelementptr [2 x i8], [2 x i8]* @"fmt_newline", i32 0, i32 0
  %"print.5" = call i32 (i8*, ...) @"printf"(i8* %"fmt_ptr.5")
  %"fmt_ptr.6" = getelementptr [3 x i8], [3 x i8]* @"fmt_int", i32 0, i32 0
  %"BANANA_val" = load i32, i32* %"BANANA"
  %"print.6" = call i32 (i8*, ...) @"printf"(i8* %"fmt_ptr.6", i32 %"BANANA_val")
  %"fmt_ptr.7" = getelementptr [2 x i8], [2 x i8]* @"fmt_newline", i32 0, i32 0
  %"print.7" = call i32 (i8*, ...) @"printf"(i8* %"fmt_ptr.7")
  %"The Code Word is: _ptr" = getelementptr [19 x i8], [19 x i8]* @"_str.The Code Word is: ", i32 0, i32 0
  %"CODE" = call i8* @"malloc"(i32 19)
  call void @"memcpy"(i8* %"CODE", i8* %"The Code Word is: _ptr", i32 19)
  %"Secret_ptr" = getelementptr [7 x i8], [7 x i8]* @"_str.Secret", i32 0, i32 0
  %"PASSWORD" = call i8* @"malloc"(i32 7)
  call void @"memcpy"(i8* %"PASSWORD", i8* %"Secret_ptr", i32 7)
  %"pt1" = call i8* @"malloc"(i32 25)
  call void @"memcpy"(i8* %"pt1", i8* %"CODE", i32 18)
  %".12" = getelementptr inbounds i8, i8* %"pt1", i32 18
  call void @"memcpy"(i8* %".12", i8* %"PASSWORD", i32 7)
  %"fmt_ptr.8" = getelementptr [3 x i8], [3 x i8]* @"fmt_string", i32 0, i32 0
  %"print.8" = call i32 (i8*, ...) @"printf"(i8* %"fmt_ptr.8", i8* %"pt1")
  %"fmt_ptr.9" = getelementptr [2 x i8], [2 x i8]* @"fmt_newline", i32 0, i32 0
  %"print.9" = call i32 (i8*, ...) @"printf"(i8* %"fmt_ptr.9")
  %"l" = alloca i32
  store i32 5, i32* %"l"
  %"m" = alloca i32
  store i32 10, i32* %"m"
  %"l_val" = load i32, i32* %"l"
  %"m_val" = load i32, i32* %"m"
  %"t.3" = mul i32 %"m_val", 500
  %"t.4" = sdiv i32 %"t.3", 2
  %"t.5" = mul i32 %"t.4", 10
  %"t.6" = add i32 %"l_val", %"t.5"
  %"g" = alloca i32
  store i32 %"t.6", i32* %"g"
  %"fmt_ptr.10" = getelementptr [3 x i8], [3 x i8]* @"fmt_int", i32 0, i32 0
  %"g_val" = load i32, i32* %"g"
  %"print.10" = call i32 (i8*, ...) @"printf"(i8* %"fmt_ptr.10", i32 %"g_val")
  %"fmt_ptr.11" = getelementptr [2 x i8], [2 x i8]* @"fmt_newline", i32 0, i32 0
  %"print.11" = call i32 (i8*, ...) @"printf"(i8* %"fmt_ptr.11")
  %"x_val.2" = load i32, i32* %"x"
  %"y_val.1" = load i32, i32* %"y"
  %"t.7" = add i32 %"x_val.2", %"y_val.1"
  %"z_val.2" = load i32, i32* %"z"
  %"t.8" = add i32 %"t.7", %"z_val.2"
  %"l_val.1" = load i32, i32* %"l"
  %"t.9" = add i32 %"t.8", %"l_val.1"
  %"m_val.1" = load i32, i32* %"m"
  %"t.10" = add i32 %"t.9", %"m_val.1"
  store i32 %"t.10", i32* %"g"
  %"fmt_ptr.12" = getelementptr [3 x i8], [3 x i8]* @"fmt_int", i32 0, i32 0
  %"g_val.1" = load i32, i32* %"g"
  %"print.12" = call i32 (i8*, ...) @"printf"(i8* %"fmt_ptr.12", i32 %"g_val.1")
  %"fmt_ptr.13" = getelementptr [2 x i8], [2 x i8]* @"fmt_newline", i32 0, i32 0
  %"print.13" = call i32 (i8*, ...) @"printf"(i8* %"fmt_ptr.13")
  %"x_val.3" = load i32, i32* %"x"
  %"y_val.2" = load i32, i32* %"y"
  %"t.11" = add i32 %"x_val.3", %"y_val.2"
  %"z_val.3" = load i32, i32* %"z"
  %"t.12" = mul i32 %"t.11", %"z_val.3"
  store i32 %"t.12", i32* %"x"
  %"fmt_ptr.14" = getelementptr [3 x i8], [3 x i8]* @"fmt_int", i32 0, i32 0
  %"x_val.4" = load i32, i32* %"x"
  %"print.14" = call i32 (i8*, ...) @"printf"(i8* %"fmt_ptr.14", i32 %"x_val.4")
  %"fmt_ptr.15" = getelementptr [2 x i8], [2 x i8]* @"fmt_newline", i32 0, i32 0
  %"print.15" = call i32 (i8*, ...) @"printf"(i8* %"fmt_ptr.15")
  ret i32 0
}

@"_str.The Code Word is: " = constant [19 x i8] c"The Code Word is: \00"
@"_str.Secret" = constant [7 x i8] c"Secret\00"