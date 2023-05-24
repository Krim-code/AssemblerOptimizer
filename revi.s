	.text
	.def	 @feat.00;
	.scl	3;
	.type	0;
	.endef
	.globl	@feat.00
.set @feat.00, 0
	.file	"<string>"
	.def	 main;
	.scl	2;
	.type	32;
	.endef
	.globl	main
	.p2align	4, 0x90
main:
.seh_proc main
	subq	$56, %rsp
	.seh_stackalloc 56
	.seh_endprologue
	movl	$0, 44(%rsp)
	movabsq	$4612811918334230528, %rax
	movq	%rax, 48(%rsp)
	movl	$2, 40(%rsp)
	leaq	fstr7472(%rip), %rcx
	movl	$2, %edx
	callq	printf
	movl	$1, %eax
	addq	$56, %rsp
	retq
	.seh_handlerdata
	.text
	.seh_endproc

	.section	.rdata,"dr"
fstr7472:
	.asciz	"%i \n"

	.globl	_fltused
