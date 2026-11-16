.text
.p2align 2
.global follow_signed_guard
follow_signed_guard:
 str x8, [sp, #0x78]
 mov w21, w26
 ldp x8, x9, [x19, #0x28]
 and x8, x8, #0x7fffffffffffffff
 and x9, x9, #0x7fffffffffffffff
 cbz x8, invalid
 cbz x9, invalid
 movz x10, #0x4066, lsl #48
 movk x10, #0x8000, lsl #32
 cmp x8, x10
 b.hs invalid
 movk x10, #0x4056, lsl #48
 cmp x9, x10
 b.hs invalid
 mov w8, #1
 str w8, [sp, #0x80]
 ldr d1, [x19, #0x30]
 b oem_resume
invalid:
 str wzr, [sp, #0x80]
 b oem_resume
