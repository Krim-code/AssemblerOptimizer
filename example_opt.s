; ModuleID = '<string>'
source_filename = "<string>"
target datalayout = "e-m:w-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "unknown-unknown-unknown"

define i32 @main() {
entry:
  %t = alloca i32, align 4
  store i32 0, i32* %t, align 4
  %t = add i32 1, 2
  store i32 %.3, i32* %t, align 4
  %.5 = add i32 2, 3
  store i32 %.5, i32* %t, align 4
  ret i32 0
}


