%define DATE 20000731
%define gcc_version 2.96
%define gcc_release 144
Summary: 2.96-RH compatibility libraries
Name: compat-gcc-296
Version: %{gcc_version}
Release: %{gcc_release}%{?dist}
License: GPLv2+
Group: Development/Languages
ExclusiveArch: %{ix86} ia64 ppc
URL: http://gcc.gnu.org
BuildRoot: /var/tmp/gcc-root
# Need .eh_frame ld optimizations
# Need proper visibility support
# Need -pie support
# Need --as-needed/--no-as-needed support
BuildRequires: binutils >= 2.15.90.0.1.1-2
BuildRequires: zlib-devel, gettext, dejagnu, bison, flex, texinfo
# Make sure pthread.h doesn't contain __thread tokens
BuildRequires: glibc-devel >= 2.2.90-12, glibc-static
# Need .eh_frame ld optimizations
# Need proper visibility support
# Need -pie support
Requires: binutils >= 2.14.90.0.4-4
# Make sure gdb will understand DW_FORM_strp
Conflicts: gdb < 5.1-2
Requires: glibc-devel >= 2.2.90-12
Requires: libgcc >= 3.4.0
Source: gcc-2.96-20000731.tar.bz2
Patch1004: gcc-c++-typedef.patch
Patch1005: gcc-no-warn-trigraphs.patch
Patch1006: gcc-incomplete-struct.patch
Patch1008: gcc-libstdc++-v3-wnoerror.patch
Patch1009: gcc-string-crash.patch
Patch1010: gcc-sparc64-subreg-byte.patch
Patch1011: gcc-sparc64-reload.patch
Patch1012: gcc-sparc64-startfile.patch
Patch1013: gcc-sparc64-decloffset.patch
Patch1014: gcc-sparc64-uname.patch
Patch1015: gcc-sparc32-vaarg.patch
Patch1016: gcc-sparc64-hwint.patch
Patch1018: gcc-java-jword.patch
Patch1019: gcc-align-memcpy.patch
Patch1020: gcc-sparcv9-hack.patch
Patch1021: gcc-stmtexpr.patch
Patch1022: gcc-sparc32-hack.patch
Patch1023: gcc-sparc32-hack2.patch
Patch1025: gcc-clear-hack.patch
Patch1028: gcc-loop.patch
Patch1029: gcc-alpha-addressof.patch
Patch1031: gcc-regmove-asm.patch
Patch1033: gcc-cpplib.patch
Patch1035: gcc-cpp0.patch
Patch1036: gcc-canon-cond.patch
Patch1037: gcc-bogus-subreg.patch
Patch1038: gcc-cp-ii.patch
Patch1039: gcc-subreg-gcse.patch
Patch1040: gcc-subregbyte-gcse.patch
Patch1041: gcc-combine-comparison.patch
Patch1042: gcc-loop-noopt.patch
Patch1043: gcc-loop-unroll.patch
Patch1044: gcc-loop-test1.patch
Patch1045: gcc-loop-test2.patch
Patch1046: gcc-loop-scanloop.patch
Patch1048: gcc-i386-ashlsilea.patch
Patch1049: gcc-i386-lea.patch
Patch1050: gcc-lowpart-test.patch
Patch1051: gcc-loop-noopt2.patch
Patch1052: gcc-i386-sibcall.patch
Patch1053: gcc-cpp-warn.patch
Patch1054: gcc-wint_t.patch
Patch1055: gcc-format-checking.patch
Patch1056: gcc-strftime.patch
Patch1057: gcc-xopen.patch
Patch1058: gcc-c99.patch
Patch1059: gcc-iso-not-ansi.patch
Patch1060: gcc-sibcall.patch
Patch1061: gcc-Os-testcase.patch
Patch1062: gcc-java-misc.patch
Patch1063: gcc-java-bytecode.patch
Patch1064: gcc-java-pg.patch
Patch1065: gcc-commutative.patch
Patch1066: gcc-relational.patch
Patch1067: gcc-f-include.patch
Patch1068: gcc-unroll.patch
Patch1069: gcc-i386-strops.patch
Patch1070: gcc-simplify-relational.patch
Patch1071: gcc-alias.patch
Patch1072: gcc-jsm1.patch
Patch1073: gcc-jsm2.patch
Patch1074: gcc-jsm3.patch
Patch1075: gcc-scanf.patch
Patch1076: gcc-jsm4.patch
Patch1077: gcc-jsm5.patch
Patch1078: gcc-jsm6.patch
Patch1079: gcc-jsm7.patch
Patch1080: gcc-jsm8.patch
Patch1081: gcc-loop-hack.patch
Patch1082: gcc-cpp-warnpaste.patch
Patch1083: gcc-float-condmove.patch
Patch1084: gcc-i386-call.patch
Patch1085: gcc-i386-call2.patch
Patch1086: gcc-i386-call-test.patch
Patch1087: gcc-i386-arith.patch
Patch1088: gcc-i386-ge_geu.patch
Patch1089: gcc-i386-gotoff.patch
Patch1090: gcc-java-catchup.patch
Patch1091: gcc-java-no-super-layout.patch
Patch1092: gcc-make-extraction.patch
Patch1093: gcc-segv1.patch
Patch1094: gcc-segv2.patch
Patch1095: gcc-sparc-copy-leaf-remappable.patch
Patch1096: gcc-wchar-const.patch
Patch1097: gcc-libio.patch
Patch1098: gcc-alpha-tune.patch
Patch1099: gcc-alpha-unaligned.patch
Patch1100: gcc-cpp-warnpaste2.patch
Patch1101: gcc-loop-giv.patch
Patch1102: gcc-real-value.patch
Patch1103: gcc-sparc-const-pool.patch
Patch1104: gcc-sparc64-timode.patch
Patch1105: gcc-callersave-segv.patch
Patch1106: gcc-libio-printf_fp.patch
Patch1107: gcc-pt-enum.patch
Patch1108: gcc-sparc-pic.patch
Patch1109: gcc-subreg-byte-expmed.patch
Patch1110: gcc-test-991206-1.patch
Patch1111: gcc-alpha-mi-thunk.patch
Patch1112: gcc-c++-pmf.patch
Patch1113: gcc-f77-fdebug.patch
Patch1114: gcc-libio-endl.patch
Patch1115: gcc-i386-compare-test.patch
Patch1116: gcc-sparc-may-trap.patch
Patch1117: gcc-sparc-mi-thunk.patch
Patch1118: gcc-c++-inline16-test.patch
Patch1119: gcc-c++-named-return-value.patch
Patch1120: gcc-c++-walk-tree.patch
Patch1121: gcc-i386-reload-test.patch
Patch1122: gcc-i386-reload.patch
Patch1123: gcc-sibcall-unchanging.patch
Patch1124: gcc-segv3.patch
Patch1125: gcc-c++-crash24.patch
Patch1126: gcc-do-store-flag.patch
Patch1127: gcc-i386-address-cost.patch
Patch1128: gcc-i386-arith2.patch
Patch1129: gcc-i386-constraint-N.patch
Patch1130: gcc-incomplete-aggregate-alias.patch
Patch1131: gcc-sibcall-eh2.patch
Patch1132: gcc-cpp-assert-crash.patch
Patch1133: gcc-c++-undefined-method.patch
Patch1134: gcc-sparc-4096.patch
Patch1135: gcc-sparc64-reload-test.patch
Patch1136: gcc-sparc64-reload2.patch
Patch1137: gcc-subreg-byte-operand-subword.patch
Patch1139: gcc-c++-static-class.patch
Patch1140: gcc-c++-testset1.patch
Patch1141: gcc-c++-testset2.patch
Patch1142: gcc-place-field.patch
Patch1143: gcc-sparc-output-formatting.patch
Patch1144: gcc-sparc64-mi-thunk.patch
Patch1145: gcc-sparc64-namedret.patch
Patch1146: gcc-sparc64-nested-fn.patch
Patch1147: gcc-c++-ice.patch
Patch1148: gcc-alpha-fold-const.patch
Patch1149: gcc-alpha-recog.patch
Patch1150: gcc-c++-pointer-to-member-test.patch
Patch1151: gcc-c++-sizetype.patch
Patch1152: gcc-cpp-64k.patch
Patch1153: gcc-cpp-empty-header.patch
Patch1154: gcc-i386-regelim.patch
Patch1155: gcc-sparc-builtin-setjmp.patch
Patch1156: gcc-test-loop-7.patch
Patch1157: gcc-c++-dump-expr.patch
Patch1158: gcc-c++-inline-cmp.patch
Patch1159: gcc-c++-inline-return.patch
Patch1160: gcc-c++-label-scope.patch
Patch1161: gcc-c++-ptm.patch
Patch1162: gcc-c++-qual-error.patch
Patch1163: gcc-const-fold.patch
Patch1164: gcc-cpp-error-directive.patch
Patch1165: gcc-i386-truncxfsf.patch
Patch1166: gcc-integrate-clobber.patch
Patch1167: gcc-libf2c-mkstemp.patch
Patch1168: gcc-local-alloc.patch
Patch1169: gcc-loop-hoistmem.patch
Patch1170: gcc-sibcall-const.patch
Patch1171: gcc-sibcall-emit-queue.patch
Patch1172: gcc-unroll-iterations.patch
Patch1173: gcc-volatile-local-var.patch
Patch1174: gcc-c++-sizetype2.patch
Patch1175: gcc-error-diagnostic.patch
Patch1176: gcc-aggregate-mode.patch
Patch1177: gcc-c++-addressof.patch
Patch1178: gcc-aggregate-mode2.patch
Patch1179: gcc-c++-addressof2.patch
Patch1180: gcc-c++-inline-cmp2.patch
Patch1181: gcc-cpp-fno-operator-names.patch
Patch1182: gcc-c++-ggc-input.patch
Patch1183: gcc-alpha-unaligned2.patch
Patch1184: gcc-alpha-ze_and_ne.patch
Patch1185: gcc-c++-wchar_t.patch
Patch1186: gcc-cpp-arg-loop.patch
Patch1187: gcc-cpp-fno-operator-names2.patch
Patch1188: gcc-cpp-g3.patch
Patch1189: gcc-fshort-wchar.patch
Patch1190: gcc-max-strlen.patch
Patch1191: gcc-stabs.patch
Patch1192: gcc-subreg-byte-gcse2.patch
Patch1193: gcc-tradcpp-MD.patch
Patch1194: gcc-alpha-expand-block-move.patch
Patch1195: gcc-c++-decl-needed.patch
Patch1196: gcc-c++-nomods_initdcl0.patch
Patch1197: gcc-cpp-MD.patch
Patch1198: gcc-fixup-var-refs.patch
Patch1199: gcc-frame-related.patch
Patch1200: gcc-i386-cmpqi.patch
Patch1201: gcc-i386-const-call-address.patch
Patch1202: gcc-i386-fcmov.patch
Patch1203: gcc-i386-sar.patch
Patch1204: gcc-c++-extern-c.patch
Patch1205: gcc-c++-inline-static.patch
Patch1206: gcc-c++-inline-static2.patch
Patch1207: gcc-cpp-M-include.patch
Patch1208: gcc-integrate-compare.patch

Source1209: gcc-cpp-20010126.tar.bz2
Patch1209: gcc-cpp-20010126.patch
Patch1210: gcc-objc-cpp-lineno.patch
Patch1211: gcc-cpp-paste-avoid.patch
Patch1212: gcc-cpp-paste-avoid2.patch

Patch1213: gcc-c++-inline-modify_expr.patch
Patch1214: gcc-i386-testqi_1.patch
Patch1215: gcc-c++-anon-union.patch
Patch1216: gcc-extract_bit_field.patch
Patch1217: gcc-c++-overload-warn.patch
Patch1218: gcc-cpp-implicit-extern-c.patch
Patch1219: gcc-cpp-paste-avoid3.patch
Patch1220: gcc-packed-enum-bitfield.patch
Patch1221: gcc-variable-size.patch

# ia64 jumbo patch
Patch1222: gcc-ia64.patch.bz2
Patch1223: gcc-ia64-errata.patch

Patch1224: gcc-cpp-defined-diag.patch
Patch1225: gcc-cpp-paste-avoid4.patch
Patch1226: gcc-dwarf2out-ice.patch
Patch1227: gcc-g++.jason-2371.patch
Patch1228: gcc-lex-line.patch
Patch1229: gcc-alpha-unaligned3.patch
Patch1230: gcc-consistency-test.patch
Source1230: gcc-consistency-test.tar.bz2
Patch1231: gcc-nested-parm.patch
Patch1232: gcc-alpha-reload.patch
Patch1233: gcc-alpha-shift.patch
Patch1234: gcc-c++-init-copy-aggr.patch
Patch1235: gcc-c++-inline-loop.patch
Patch1236: gcc-c++-lookup.patch
Patch1237: gcc-c++-taking-address-error.patch
Patch1238: gcc-objc-gc.patch
Patch1239: gcc-objc-test.patch
Patch1240: gcc-reload-hardreg-free.patch
Patch1241: gcc-cpp-20010222.patch
Patch1242: gcc-expr-safety.patch
Patch1243: gcc-debug-static-local.patch
Patch1244: gcc-fixup-var-refs2.patch
Patch1245: gcc-fold-const-div.patch
Patch1246: gcc-g77-unused.patch
Patch1247: gcc-ia64-flushrs.patch
Patch1248: gcc-ia64-syscall-linkage.patch
Patch1249: gcc-recog-addressof.patch
Patch1250: gcc-cpp-20010309.patch
Patch1251: gcc-cant-combine.patch
Patch1252: gcc-i386-crtendS.patch
Patch1253: gcc-reg-stack-clobber.patch
Patch1254: gcc-reg-stack.patch
Patch1255: gcc-store-expr.patch
Patch1256: gcc-target-expr.patch
Patch1257: gcc-c++-anonaggr-copy.patch
Patch1258: gcc-c++-asmspec.patch
Patch1259: gcc-c++-static-local.patch
Patch1260: gcc-f77-line.patch
Patch1261: gcc-libstdc++-getline.patch
Patch1262: gcc-no-new-abi.patch
Patch1263: gcc-regrename.patch
Patch1264: gcc-subreg-byte-gcse3.patch
Patch1265: gcc-wshadow-doc.patch
Patch1266: gcc-c++-D__EXCEPTIONS.patch
Patch1267: gcc-c++-throttle-inline.patch
Patch1268: gcc-fold-pointer-cmp.patch
Patch1269: gcc-ifcvt-strict-low-part.patch
Patch1270: gcc-gcse-reg-equiv.patch
Patch1271: gcc-null-pointer-check.patch
Patch1272: gcc-local-inline.patch
Patch1273: gcc-cpp-Wcomment.patch
Patch1274: gcc-cselib-mode.patch
Patch1275: gcc-dwarf2-O0-crash.patch
Patch1276: gcc-dwarf2out-splice-child.patch
Patch1277: gcc-i386-movcc.patch
Patch1278: gcc-ia64-xdata.patch
Patch1279: gcc-subregbyte-hard-regno.patch
Patch1280: gcc-tradtradcpp0.patch
Patch1281: gcc-flow-autoinc.patch
Patch1282: gcc-ia64-constconst.patch
Patch1283: gcc-ia64-G.patch
Patch1284: gcc-integrate-error.patch
Patch1285: gcc-MD-nodot.patch
Patch1286: gcc-store-constructor-field.patch
Patch1287: gcc-ia64-except.patch
Patch1288: gcc-ia64-loc79.patch
Patch1289: gcc-ia64-bstep.patch
Patch1290: gcc-c++-templ-arg.patch
Patch1291: gcc-frame-state-for-compat.patch
Patch1292: gcc-sibcall-catch.patch
Patch1293: gcc-tradcpp-define.patch
Patch1294: gcc-c++-inline-method.patch
Patch1295: gcc-gcse-trapping.patch
Patch1296: gcc-nested-expr-stmt.patch
Patch1297: gcc-__NO_INLINE__.patch
Patch1298: gcc-bogus-inline.patch
Patch1299: gcc-c++-defarg.patch
Patch1300: gcc-c++-instantiate.patch
Patch1301: gcc-c++-static-ctordtor.patch
Patch1302: gcc-c++-templ-arg2.patch
Patch1303: gcc-c++-ucs.patch
Patch1304: gcc-fsyntax-only.patch
Patch1305: gcc-g77-unsigned-char.patch
Patch1306: gcc-hash-ident.patch
Patch1307: gcc-jump-threading.patch
Patch1308: gcc-regmove-unchanging.patch
Patch1309: gcc-ia64-complex-float.patch
Patch1310: gcc-ia64-movcc-fail.patch
Patch1311: gcc-ia64-stop-bit.patch
Patch1312: gcc-c++-friend.patch
Patch1313: gcc-i386-stack-adjust.patch
Patch1314: gcc-SHF_MERGE.patch
Patch1315: gcc-dwarf2-filenames.patch
Patch1316: gcc-k6-loop.patch
Patch1317: gcc-libobjc-3.0.patch
Patch1318: gcc-texinfo-texconfig.patch
Patch1319: gcc-c++-complext.patch
Patch1320: gcc-c++-conv-cv-ptr.patch
Patch1321: gcc-c++-sstream-warn.patch
Patch1322: gcc-f77-ffixed.patch
Patch1323: gcc-invalid-stabs.patch
Patch1324: gcc-libio-test.patch
Patch1325: gcc-alpha-function-sections.patch
Patch1326: gcc-alpha-vtable-gc.patch
Patch1327: gcc-c++-anontypename.patch
Patch1328: gcc-c++-array-cast.patch
Patch1329: gcc-c++-colonequal.patch
Patch1330: gcc-c++-cond-ovl.patch
Patch1331: gcc-c++-weak-address.patch
Patch1332: gcc-libio-input-float.patch
Patch1333: gcc-subreg-byte-stabs.patch
Patch1334: gcc-c++-array-side-effects.patch
Patch1335: gcc-cpp-memleak.patch
Patch1336: gcc-c++-template-throw.patch
Patch1337: gcc-c++-tsubst-friend-class.patch
Patch1338: gcc-dwarf2-debug-line.patch
Patch1339: gcc-ifcvt-eh.patch
Patch1340: gcc-ia64-vararg.patch
Patch1341: gcc-gcse-hoist.patch
Patch1342: gcc-ia64-eh.patch
Patch1343: gcc-libio-stdstream-offset.patch
Patch1344: gcc-objc-class-ref.patch
Patch1345: gcc-tail-recurse.patch
Patch1346: gcc-c++-sstream-seek.patch
Patch1347: gcc-loop-combine-givs.patch
Patch1348: gcc-alpha-asm-input.patch
Patch1349: gcc-c++-anon-union2.patch
Patch1350: gcc-c++-inline-sizeof-char.patch
Patch1351: gcc-cpp-run-directive.patch
Patch1352: gcc-reload-optional.patch
Patch1353: gcc-fde-merge-compat.patch
Patch1354: gcc-flow-setjmp.patch
Patch1355: gcc-pure-reload.patch
Patch1356: gcc-sparc-float.patch
Patch1357: gcc-sparc-movdf.patch
Patch1358: gcc-c++-member-init.patch
Patch1359: gcc-autoconf-2.52.patch
Patch1360: gcc-makej.patch
Patch1361: gcc-ia64-bitfield-return.patch
Patch1362: gcc-ia64-NaT.patch
Patch1363: gcc-sparc-libcall.patch
Patch1364: gcc-c++-preexpand-calls.patch
Patch1365: gcc-libio-stdstreams-vptr.patch
Patch1366: gcc-sparc-return.patch
Patch1367: gcc-sparc64-nonzero-bits.patch
Patch1368: gcc-below-sp.patch
Patch1369: gcc-c++-setup-vtbl-ptr.patch
Patch1370: gcc-reload-ofp.patch
Patch1371: gcc-bitop-shorten.patch
Patch1372: gcc-c++-ptrintsum.patch
Patch1373: gcc-i386-fxch.patch
Patch1374: gcc-i386-regparm-struct.patch
Patch1375: gcc-ia64-encode-section-info.patch
Patch1376: gcc-attr-visibility.patch
Patch1377: gcc-store_field-expand_and.patch
Patch1378: gcc-c++-array-ref.patch
Patch1379: gcc-c++-flat-initializer.patch
Patch1380: gcc-c++-static-member.patch
Patch1381: gcc-i386-reg-stack-check.patch
Patch1382: gcc-i386-zero-size.patch
Patch1383: gcc-loop-check_dbra_loop.patch
Patch1384: gcc-pedwarn-string-length.patch
Patch1385: gcc-simplify-check-overflow.patch
Patch1386: gcc-UDA-option-order.patch
Patch1387: gcc-c++-pt-using.patch
Patch1388: gcc-c++-pt-using2.patch
Patch1389: gcc-attr-visibility2.patch
Patch1390: gcc-libstdc++-libc-interface.patch
Patch1391: gcc-attr-visibility3.patch
Patch1392: gcc-ia64-thread-safe-eh.patch
Patch1393: gcc-merge_blocks_nomove.patch
Patch1394: gcc-attr-visibility4.patch
Patch1395: gcc-unaligned-const.patch
Patch1396: gcc-i386-piclabel.patch
Patch1397: gcc-2.96-parallel.patch
Patch1398: gcc-i386-andhi.patch
Patch1399: gcc-mem-scratch.patch
Patch1400: gcc-unroll2.patch
Patch1401: gcc-sparc-tfdi.patch
Patch1402: gcc-c++-gc-named-label-list.patch
Patch1403: gcc-cpp-include-dir.patch
Patch1404: gcc-c++-compound-literal.patch
Patch1405: gcc-c++-eh-spec-incomplete.patch
Patch1406: gcc-fde-merge-compat-2.patch
Patch1407: gcc-strict-alias-optimization.patch
Patch1408: gcc-cpp-MD-2.patch
Patch1409: gcc-libstdc++-wchar.patch
Patch1410: gcc-ia64-frame-leak.patch
Patch1411: gcc-libstdc++-wchar-fix.patch
Patch1412: gcc-memfn-addr.patch
Patch1413: gcc-bogus-addressof.patch
Patch1414: gcc-libstdc++-wchar-c_str.patch
Patch1415: gcc-reload-unchanging.patch
Patch1416: gcc-store-constructor.patch
Patch1417: gcc-strict-alias-optimization2.patch
Patch1418: gcc-libstdc++-thread-safety.patch
Patch1419: gcc-libstdc++-std-compare.patch
Patch1420: gcc-libstdc++-stl-alloc.patch
Patch1421: gcc-forget-old-reloads.patch
Patch1422: gcc-ia64-noreturn-eh.patch

Patch1450: gcc-bison.patch
Patch1451: gcc-trap-0.patch
Patch1452: gcc-rodata-jumptables.patch
Patch1453: gcc-gcc4-compile.patch

Patch1500: gcc-libg++-config.patch

%define _gnu %{nil}

%description
This package contains no files, but is used to build compat-libstdc++-296
and compat-libgcc-296.

%package -n compat-libstdc++-296
Summary: Compatibility 2.96-RH standard C++ libraries
Group: System Environment/Libraries
Obsoletes: compat-libstdc++

%description -n compat-libstdc++-296
The compat-libstdc++-296 package contains 2.96-RH compatibility standard
C++ libraries.

%package -n compat-libgcc-296
Summary: Compatibility 2.96-RH libgcc library
Group: Development/Languages
Obsoletes: gcc <= 2.96
Obsoletes: compat-gcc

%description -n compat-libgcc-296
The compat-libgcc-296 package contains 2.96-RH libgcc.a library and support
object files.

%prep
%setup -q -n gcc-%{gcc_version}-%{DATE}
%patch1010 -p0 -b .sparc
%patch1011 -p0 -b .sparc1
%patch1012 -p0 -b .sparc2
%patch1013 -p0 -b .sparc3
%patch1014 -p0 -b .sparc4
%patch1015 -p0 -b .sparc5
%patch1016 -p0 -b .sparc6
%patch1018 -p0 -b .jword
%patch1019 -p0 -b .memcpy
%patch1020 -p0 -b .sparcv9
%patch1004 -p0 -b .typedef
%patch1005 -p0 -b .trigraph
%patch1006 -p0 -b .incompl
%patch1008 -p0 -b .wnoerror
%patch1009 -p0 -b .stringcrash
%patch1021 -p0 -b .stmtexpr
%ifarch sparc
#%patch1022 -p0 -b .sparc32hack
if [ ! -f /usr/lib64/crt1.o ]; then
%patch1023 -p0 -b .sparc32hack2
fi
%endif
#%patch1025 -p0 -b .hack
%patch1028 -p0 -b .loop
%patch1029 -p0 -b .addressof
%patch1031 -p0 -b .regmoveasm
%patch1033 -p0 -b .cpplib
%patch1035 -p0 -b .cpp0
%patch1036 -p0 -b .canoncond
%patch1037 -p0 -b .bogussubreg
%patch1038 -p0 -b .cpii
%patch1039 -p0 -b .subreggcse
%patch1040 -p0 -b .subregbytegcse
%patch1041 -p0 -b .combinecomparison
%patch1042 -p0 -b .loopnoopt
%patch1043 -p0 -b .loopunroll
%patch1044 -p0 -b .looptest1
%patch1045 -p0 -b .looptest2
%patch1046 -p0 -b .loopscanloop
%patch1048 -p0 -b .ashlsilea
%patch1049 -p0 -b .lea
%patch1050 -p0 -b .lowparttest
%patch1051 -p0 -b .loopnoopt2
%patch1052 -p0 -b .i386sib
%patch1053 -p0 -b .cppwarn
%patch1054 -p0 -b .wintt
%patch1055 -p0 -b .fmtchk
%patch1056 -p0 -b .strftime
%patch1057 -p0 -b .xopen
%patch1058 -p0 -b .c99std
%patch1059 -p0 -b .iso-not-ansi
%patch1060 -p0 -b .sibcall
%patch1061 -p0 -b .ostest
%patch1062 -p0 -b .java-misc
%patch1063 -p0 -b .java-bytecode
%patch1064 -p0 -b .java-pg
# These two are buggy
#%patch1065 -p0 -b .cmtable
#%patch1066 -p0 -b .relational
%patch1067 -p0 -b .finclude
%patch1068 -p0 -b .unroll
%patch1069 -p0 -b .i386-strops
%patch1070 -p0 -b .simplify-rela
%patch1071 -p0 -b .alias
%patch1072 -p0 -b .jsm1
%patch1073 -p0 -b .jsm2
%patch1074 -p0 -b .jsm3
%patch1075 -p0 -b .scanf
%patch1076 -p0 -b .jsm4
%patch1077 -p0 -b .jsm5
%patch1078 -p0 -b .jsm6
%patch1079 -p0 -b .jsm7
%patch1080 -p0 -b .jsm8
%patch1081 -p0 -b .loop-hack
%patch1082 -p0 -b .cpp-warnpaste
%patch1083 -p0 -b .float-condmove
%patch1084 -p0 -b .i386-call
%patch1085 -p0 -b .i386-call2
%patch1086 -p0 -b .i386-call-test
%patch1087 -p0 -b .i386-arith
%patch1088 -p0 -b .i386-ge_geu
%patch1089 -p0 -b .i386-gotoff
%patch1090 -p0 -b .java-catchup
%patch1091 -p0 -b .java-no-super-layout
%patch1092 -p0 -b .make-extraction
%patch1093 -p0 -b .segv1
%patch1094 -p0 -b .segv2
%patch1095 -p0 -b .copy-leaf-remap
%patch1096 -p0 -b .wchar-const
%patch1097 -p0 -b .libio
%patch1098 -p0 -b .alpha-tune
%patch1099 -p0 -b .alpha-unaligned
%patch1100 -p0 -b .cpp-warnpaste2
%patch1101 -p0 -b .loop-giv
%patch1102 -p0 -b .real-value
%patch1103 -p0 -b .sparc-const-pool
%patch1104 -p0 -b .sparc64-timode
%patch1105 -p0 -b .callersave-segv
%patch1106 -p0 -b .libio-printf_fp
%patch1107 -p0 -b .pt-enum
%patch1108 -p0 -b .sparc-pic
%patch1109 -p0 -b .subreg-byte-expmed
%patch1110 -p0 -b .test-991206-1
%patch1111 -p0 -b .alpha-mi-thunk
%patch1112 -p0 -b .c++-pmf
%patch1113 -p0 -b .f77-fdebug
%patch1114 -p0 -b .libio-endl
%patch1115 -p0 -b .i386-compare-test
%patch1116 -p0 -b .sparc-may-trap
%patch1117 -p0 -b .sparc-mi-thunk
%patch1118 -p0 -b .c++-inline16-test
%patch1119 -p0 -b .c++-named-return-value
%patch1120 -p0 -b .c++-walk-tree
%patch1121 -p0 -b .i386-reload-test
%patch1122 -p0 -b .i386-reload
%patch1123 -p0 -b .sibcall-unchanging
%patch1124 -p0 -b .segv3
%patch1125 -p0 -b .c++-crash24
%patch1126 -p0 -b .do-store-flag
%patch1127 -p0 -b .i386-address-cost
%patch1128 -p0 -b .i386-arith2
%patch1129 -p0 -b .i386-constraint-N
%patch1130 -p0 -b .incomplete-aggregate-alias
%patch1131 -p0 -b .sibcall-eh2
%patch1132 -p0 -b .cpp-assert-crash
%patch1133 -p0 -b .c++-undefined-method
%patch1134 -p0 -b .sparc-4096
%patch1135 -p0 -b .sparc64-reload-test
%patch1136 -p0 -b .sparc64-reload2
%patch1137 -p0 -b .subreg-byte-operand-subword
%patch1139 -p0 -b .c++-static-class
%patch1140 -p0 -b .c++-testset1
%patch1141 -p0 -b .c++-testset2
%patch1142 -p0 -b .place-field
%patch1143 -p0 -b .sparc-output-formatting
%patch1144 -p0 -b .sparc64-mi-thunk
%patch1145 -p0 -b .sparc64-namedret
%patch1146 -p0 -b .sparc64-nested-fn
%patch1147 -p0 -b .c++-ice
%patch1148 -p0 -b .alpha-fold-const
%patch1149 -p0 -b .alpha-recog
%patch1150 -p0 -b .c++-pointer-to-member-test
%patch1151 -p0 -b .c++-sizetype
%patch1152 -p0 -b .cpp-64k
%patch1153 -p0 -b .cpp-empty-header
%patch1154 -p0 -b .i386-regelim
%patch1155 -p0 -b .sparc-builtin-setjmp
%patch1156 -p0 -b .test-loop-7
%patch1157 -p0 -b .c++-dump-expr
%patch1158 -p0 -b .c++-inline-cmp
%patch1159 -p0 -b .c++-inline-return
%patch1160 -p0 -b .c++-label-scope
%patch1161 -p0 -b .c++-ptm
%patch1162 -p0 -b .c++-qual-error
%patch1163 -p0 -b .const-fold
%patch1164 -p0 -b .cpp-error-directive
%patch1165 -p0 -b .i386-truncxfsf
%patch1166 -p0 -b .integrate-clobber
%patch1167 -p0 -b .libf2c-mkstemp
%patch1168 -p0 -b .local-alloc
%patch1169 -p0 -b .loop-hoistmem
%patch1170 -p0 -b .sibcall-const
%patch1171 -p0 -b .sibcall-emit-queue
%patch1172 -p0 -b .unroll-iterations
%patch1173 -p0 -b .volatile-local-var
%patch1174 -p0 -b .c++-sizetype2
%patch1175 -p0 -b .error-diagnostic
%patch1176 -p0 -b .aggregate-mode
%patch1177 -p0 -b .c++-addressof
%patch1178 -p0 -b .aggregate-mode2
%patch1179 -p0 -b .c++-addressof2
%patch1180 -p0 -b .c++-inline-cmp2
%patch1181 -p0 -b .cpp-fno-operator-names
%patch1182 -p0 -b .c++-ggc-input
%patch1183 -p0 -b .alpha-unaligned2
%patch1184 -p0 -b .alpha-ze_and_ne
%patch1185 -p0 -b .c++-wchar_t
%patch1186 -p0 -b .cpp-arg-loop
%patch1187 -p0 -b .cpp-fno-operator-names2
%patch1188 -p0 -b .cpp-g3
%patch1189 -p0 -b .fshort-wchar
%patch1190 -p0 -b .max-strlen
%patch1191 -p0 -b .stabs
%patch1192 -p0 -b .subreg-byte-gcse2
%patch1193 -p0 -b .tradcpp-MD
%patch1194 -p0 -b .alpha-expand-block-move
%patch1195 -p0 -b .c++-decl-needed
%patch1196 -p0 -b .c++-nomods_initdcl0
%patch1197 -p0 -b .cpp-MD
%patch1198 -p0 -b .fixup-var-refs
%patch1199 -p0 -b .frame-related
%patch1200 -p0 -b .i386-cmpqi
%patch1201 -p0 -b .i386-const-call-address
%patch1202 -p0 -b .i386-fcmov
%patch1203 -p0 -b .i386-sar
%patch1204 -p0 -b .c++-extern-c
%patch1205 -p0 -b .c++-inline-static
%patch1206 -p0 -b .c++-inline-static2
%patch1207 -p0 -b .cpp-M-include
%patch1208 -p0 -b .integrate-compare
# Put in cpp snapshot from 20010126
rm -rf gcc/testsuite/gcc.dg/cpp
tar x --bzip2 -f %{SOURCE1209}
%patch1209 -p0 -b .cpp-20010126
%patch1210 -p0 -b .objc-cpp-lineno
%patch1211 -p0 -b .cpp-paste-avoid
%patch1212 -p0 -b .cpp-paste-avoid2
# Bug fixing continues
%patch1213 -p0 -b .c++-inline-modify_expr
%patch1214 -p0 -b .i386-testqi_1
%patch1215 -p0 -b .c++-anon-union
%patch1216 -p0 -b .extract_bit_field
%patch1217 -p0 -b .c++-overload-warn
%patch1218 -p0 -b .cpp-implicit-extern-c
%patch1219 -p0 -b .cpp-paste-avoid3
%patch1220 -p0 -b .packed-enum-bitfield
%patch1221 -p0 -b .variable-size
%ifarch ia64
%patch1222 -p0 -b .ia64
%patch1223 -p0 -b .ia64-errata
%endif

%patch1224 -p0 -b .cpp-defined-diag
%patch1225 -p0 -b .cpp-paste-avoid4
%patch1226 -p0 -b .dwarf2out-ice
%patch1227 -p0 -b .g++.jason-2371
%patch1228 -p0 -b .lex-line
%patch1229 -p0 -b .alpha-unaligned3
tar x --bzip2 -f %{SOURCE1230}
%patch1230 -p0 -b .consistency
%patch1231 -p0 -b .nested-parm
%patch1232 -p0 -b .alpha-reload
%patch1233 -p0 -b .alpha-shift
%patch1234 -p0 -b .c++-init-copy-aggr
%patch1235 -p0 -b .c++-inline-loop
%patch1236 -p0 -b .c++-lookup
%patch1237 -p0 -b .c++-taking-address-error
%patch1238 -p0 -b .objc-gc
%patch1239 -p0 -b .objc-test
%patch1240 -p0 -b .reload-hardreg-free
%patch1241 -p0 -b .cpp-20010222
%patch1242 -p0 -b .expr-safety
%patch1243 -p0 -b .debug-static-local
%patch1244 -p0 -b .fixup-var-refs2
%patch1245 -p0 -b .fold-const-div
%patch1246 -p0 -b .g77-unused
%ifarch ia64
%patch1247 -p0 -b .ia64-flushrs
%patch1248 -p0 -b .ia64-syscall-linkage
%endif
%patch1249 -p0 -b .recog-addressof
%patch1250 -p0 -b .cpp-20010309
%patch1251 -p0 -b .cant-combine
%patch1252 -p0 -b .i386-crtendS
%patch1253 -p0 -b .reg-stack-clobber
%patch1254 -p0 -b .reg-stack
%patch1255 -p0 -b .store-expr
%patch1256 -p0 -b .target-expr
%patch1257 -p0 -b .c++-anonaggr-copy
%patch1258 -p0 -b .c++-asmspec
%patch1259 -p0 -b .c++-static-local
%patch1260 -p0 -b .f77-line
%patch1261 -p0 -b .libstdc++-getline
%patch1262 -p0 -b .no-new-abi
%patch1263 -p0 -b .regrename
%patch1264 -p0 -b .subreg-byte-gcse3
%patch1265 -p0 -b .wshadow-doc
%patch1266 -p0 -b .c++-D__EXCEPTIONS
%patch1267 -p0 -b .c++-throttle-inline
%patch1268 -p0 -b .fold-pointer-cmp
%patch1269 -p0 -b .ifcvt-strict-low-part
%patch1270 -p0 -b .gcse-reg-equiv
%patch1271 -p0 -b .null-pointer-check
%patch1272 -p0 -b .local-inline
%patch1273 -p0 -b .cpp-Wcomment
%patch1274 -p0 -b .cselib-mode
%patch1275 -p0 -b .dwarf2-O0-crash
%patch1276 -p0 -b .dwarf2out-splice-child
%patch1277 -p0 -b .i386-movcc
%patch1278 -p0 -b .ia64-xdata
%patch1279 -p0 -b .subregbyte-hard-regno
%patch1280 -p0 -b .tradtradcpp0
%patch1281 -p0 -b .flow-autoinc
%patch1282 -p0 -b .ia64-constconst
%patch1283 -p0 -b .ia64-G
%patch1284 -p0 -b .integrate-error
%patch1285 -p0 -b .MD-nodot
%patch1286 -p0 -b .store-constructor-field
%ifarch ia64
%patch1287 -p0 -b .ia64-expect
%patch1288 -p0 -b .ia64-loc79
# Add -mb-step automatically -- this will go away when production
# hardware is available.
%patch1289 -p0 -b .ia64-bstep
%endif
%patch1290 -p0 -b .c++-templ-arg
%patch1291 -p0 -b .frame-state-for-compat
%patch1292 -p0 -b .sibcall-catch
%patch1293 -p0 -b .tradcpp-define
%patch1294 -p0 -b .c++-inline-method
%patch1295 -p0 -b .gcse-trapping
%patch1296 -p0 -b .nested-expr-stmt
%patch1297 -p0 -b .__NO_INLINE__
%patch1298 -p0 -b .bogus-inline
%patch1299 -p0 -b .c++-defarg
%patch1300 -p0 -b .c++-instantiate
%patch1301 -p0 -b .c++-static-ctordtor
%patch1302 -p0 -b .c++-templ-arg2
%patch1303 -p0 -b .c++-ucs
%patch1304 -p0 -b .fsyntax-only
%patch1305 -p0 -b .g77-unsigned-char
%patch1306 -p0 -b .hash-ident
#%patch1307 -p0 -b .jump-threading
%patch1308 -p0 -b .regmove-unchanging
%ifarch ia64
%patch1309 -p0 -b .ia64-complex-float
%patch1310 -p0 -b .ia64-movcc-fail
%patch1311 -p0 -b .ia64-stop-bit
%endif
%patch1312 -p0 -b .c++-friend
%patch1313 -p0 -b .i386-stack-adjust
%patch1314 -p0 -b .SHF_MERGE
%patch1315 -p0 -b .dwarf2-filenames
%patch1316 -p0 -b .k6-loop
%patch1317 -p0 -b .libobjc-3.0
%patch1318 -p0 -b .texinfo-texconfig
%patch1319 -p0 -b .c++-complext
%patch1320 -p0 -b .c++-conv-cv-ptr
%patch1321 -p0 -b .c++-sstream-warn
%patch1322 -p0 -b .f77-ffixed
%patch1323 -p0 -b .invalid-stabs
%patch1324 -p0 -b .libio-test
%patch1325 -p0 -b .alpha-function-sections
%patch1326 -p0 -b .alpha-vtable-gc
%patch1327 -p0 -b .c++-anontypename
%patch1328 -p0 -b .c++-array-cast
%patch1329 -p0 -b .c++-colonequal
%patch1330 -p0 -b .c++-cond-ovl
%patch1331 -p0 -b .c++-weak-address
%patch1332 -p0 -b .libio-input-float
%patch1333 -p0 -b .subreg-byte-stabs
%patch1334 -p0 -b .c++-array-side-effects
%patch1335 -p0 -b .cpp-memleak
%patch1336 -p0 -b .c++-template-throw
%patch1337 -p0 -b .c++-tsubst-friend-class
%patch1338 -p0 -b .dwarf2-debug-line
%patch1339 -p0 -b .ifcvt-eh
%patch1340 -p0 -b .ia64-vararg
%patch1341 -p0 -b .gcse-hoist
%ifarch ia64
%patch1342 -p0 -b .ia64-eh
%endif
%patch1343 -p0 -b .libio-stdstream-offset
%patch1344 -p0 -b .objc-class-ref
%patch1345 -p0 -b .tail-recurse
%patch1346 -p0 -b .c++-sstream-seek
%patch1347 -p0 -b .loop-combine-givs
%patch1348 -p0 -b .alpha-asm-input
%patch1349 -p0 -b .c++-anon-union2
%patch1350 -p0 -b .c++-inline-sizeof-char
%patch1351 -p0 -b .cpp-run-directive
%patch1352 -p0 -b .reload-optional
%patch1353 -p0 -b .fde-merge-compat
%patch1354 -p0 -b .flow-setjmp
%patch1355 -p0 -b .pure-reload
%patch1356 -p0 -b .sparc-float
%patch1357 -p0 -b .sparc-movdf
%patch1358 -p0 -b .c++-member-init
%patch1359 -p0 -b .autoconf-2.52
%patch1360 -p0 -b .makej
%ifarch ia64
%patch1361 -p0 -b .ia64-bitfield-return
%patch1362 -p0 -b .ia64-NaT
%endif
%ifarch sparc sparc64
%patch1363 -p0 -b .sparc-libcall
%endif
#%patch1364 -p0 -b .c++-preexpand-calls
%patch1365 -p0 -b .libio-stdstreams-vptr
%patch1366 -p0 -b .sparc-return
%patch1367 -p0 -b .sparc64-nonzero-bits
%patch1368 -p0 -b .below-sp
%patch1369 -p0 -b .c++-setup-vtbl-ptr
%patch1370 -p0 -b .reload-ofp
%patch1371 -p0 -b .bitop-shorten
%patch1372 -p0 -b .c++-ptrintsum
%patch1373 -p0 -b .i386-fxch
%patch1374 -p0 -b .i386-regparm-struct
%patch1375 -p0 -b .ia64-encode-section-info
%patch1376 -p0 -b .attr-visibility
%patch1377 -p0 -b .store_field-expand_and
%patch1378 -p0 -b .c++-array-ref
%patch1379 -p0 -b .c++-flat-initializer
%patch1380 -p0 -b .c++-static-member
%patch1381 -p0 -b .i386-reg-stack-check
%patch1382 -p0 -b .i386-zero-size
%patch1383 -p0 -b .loop-check_dbra_loop
%patch1384 -p0 -b .pedwarn-string-length
%patch1385 -p0 -b .simplify-check-overflow
%patch1386 -p0 -b .UDA-option-order
%patch1387 -p0 -b .c++-pt-using
%patch1388 -p0 -b .c++-pt-using2
%patch1389 -p0 -b .attr-visibility2
%patch1390 -p0 -b .libstdc++-libc-interface
%patch1391 -p0 -b .attr-visibility3
%ifarch ia64
%patch1392 -p0 -b .ia64-thread-safe-eh
%endif
%patch1393 -p0 -b .merge_blocks_nomove
%patch1394 -p0 -b .attr-visibility4
%ifarch ia64
%patch1395 -p0 -b .unaligned-const
%endif
%patch1396 -p0 -b .i386-piclabel
%patch1397 -p0 -b .2.96-parallel
%patch1398 -p0 -b .i386-andhi
%patch1399 -p0 -b .mem-scratch
%patch1400 -p0 -b .unroll2
%patch1401 -p0 -b .sparc-tfdi
%patch1402 -p0 -b .c++-gc-named-label-list
%patch1403 -p0 -b .cpp-include-dir
%patch1404 -p0 -b .c++-compound-literal
%patch1405 -p0 -b .c++-eh-spec-incomplete
%patch1406 -p0 -b .fde-merge-compat-2
%patch1407 -p0 -b .strict-alias-optimization
%patch1408 -p0 -b .cpp-MD-2
%ifarch %{ix86} alpha ia64
%patch1409 -p0 -b .libstdc++-wchar
%endif
%ifarch ia64
%patch1410 -p0 -b .ia64-frame-leak
%endif
%ifarch %{ix86} alpha ia64
%patch1411 -p0 -b .libstdc++-wchar-fix
%endif
%patch1412 -p0 -b .memfn-addr
%patch1413 -p0 -b .bogus-addressof
%ifarch %{ix86} alpha ia64
%patch1414 -p0 -b .libstdc++-wchar-c_str
%endif
%patch1415 -p0 -b .reload-unchanging
%patch1416 -p0 -b .store-constructor
%patch1417 -p0 -b .strict-alias-optimization2
%patch1418 -p0 -b .libstdc++-thread-safety
%ifarch %{ix86} alpha ia64
%patch1419 -p0 -b .libstdc++-std-compare
%endif
%patch1420 -p0 -b .libstdc++-stl-alloc
%patch1421 -p0 -b .forget-old-reloads
%ifarch ia64
%patch1422 -p0 -b .ia64-noreturn-eh
%endif

%patch1450 -p0 -b .bison~
%patch1451 -p0 -b .trap-0~
%patch1452 -p0 -b .rodata-jumptables~
%patch1453 -p0 -b .gcc4-compile~

perl -pi -e 's/\(experimental\)/\(Red Hat Linux 7.3 %{gcc_version}-%{gcc_release}\)/' gcc/version.c gcc/f/version.c
perl -pi -e 's/#define GCCBUGURL.*$/#define GCCBUGURL "<URL:http:\/\/bugzilla.redhat.com\/bugzilla\/>"/' gcc/system.h
perl -pi -e 's/^ALL_CFLAGS = /ALL_CFLAGS = -fPIC /' `find libf2c -name Makefile.in`
# Link libstdc++ against libgcc_s
mkdir libgcc
%ifarch sparc64
mkdir libgcc/32
ln -sf /lib64/libgcc_s.so.1 libgcc/libgcc_s.so
ln -sf /lib/libgcc_s.so.1 libgcc/32/libgcc_s.so
%else
%ifarch sparc
mkdir libgcc/64
ln -sf /lib64/libgcc_s.so.1 libgcc/64/libgcc_s.so
ln -sf /lib/libgcc_s.so.1 libgcc/libgcc_s.so
%else
ln -sf /lib/libgcc_s.so.1 libgcc/libgcc_s.so
%endif
%endif
cp -a libstdc++/Makefile.in libstdc++/Makefile.in.tmp
sed 's@(SHDEPS)@(SHDEPS) -L'`pwd`'/libgcc -lgcc_s@' libstdc++/Makefile.in.tmp > libstdc++/Makefile.in
rm -f libstdc++/Makefile.in.tmp
# FIX SHF_MERGE stuff so that it uses "aMS" and "aM" instead of "ams" and "am"
perl -pi -e 's/"ams/"aMS/' gcc/configure.in gcc/configure gcc/config/elfos.h gcc/config/alpha/elf.h
perl -pi -e 's/"am/"aM/' gcc/configure.in gcc/configure gcc/config/elfos.h gcc/config/alpha/elf.h
touch gcc/c-parse.h gcc/cp/parse.h gcc/tradcif.c
touch gcc/cstamp-h.in gcc/config.in

%ifarch ppc
sed -ie 's@-lgcc_s@-lgcc_s -lnldbl_nonshared@' libstdc++/Makefile.in
%endif

%build
rm -fr obj-%{_target_platform}
mkdir obj-%{_target_platform}
cd obj-%{_target_platform}
mkdir ld_hack
cat > ld_hack/ld <<\EOF
#!/bin/sh
case " $* " in *\ -r\ *) exec /usr/bin/ld "$@";; esac
exec /usr/bin/ld --build-id -z noexecstack "$@"
EOF
chmod 755 ld_hack/ld
export PATH=`pwd`/ld_hack/${PATH:+:$PATH}

CC=gcc
OPT_FLAGS=`echo $RPM_OPT_FLAGS|sed -e 's/-fno-rtti//g' -e 's/-fno-exceptions//g' -e s/-g//`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-m64//g;s/-m32//g;s/-m31//g'`
%ifarch %{ix86}
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-mtune=pentium4/-mcpu=i686/g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-mtune=generic/-mcpu=i686/g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-mtune=atom/-mcpu=i686/g'`
%endif
%ifarch sparc sparc64
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-mcpu=ultrasparc/-mtune=ultrasparc/g'`
%endif
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-Wall//g' -e 's/-Wp,-D_FORTIFY_SOURCE=2//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-fexceptions//g' -e 's/-fasynchronous-unwind-tables//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-fstack-protector//g' -e 's/--param=ssp-buffer-size=[0-9]*//g'`
%ifarch ia64
rm -f ../gcc/ChangeLog*.ia64
%endif
CC="$CC" CFLAGS="$OPT_FLAGS" CXXFLAGS="$OPT_FLAGS" XCFLAGS="$OPT_FLAGS" \
        TCFLAGS="$OPT_FLAGS" \
        ../configure --prefix=%{_prefix} --mandir=%{_mandir} --infodir=%{_infodir} \
        --enable-shared --enable-threads=posix --enable-haifa --disable-checking \
	--enable-languages=c,c++ \
        --host=%{_target_platform}

touch ../gcc/c-gperf.h

abifile=
%ifarch %{ix86}
abifile=i386-redhat-linux.txt
%endif
%ifarch alpha
abifile=alpha-redhat-linux.txt
%endif
%ifarch ia64
abifile=ia64-redhat-linux.txt
%endif
if [ -n "$abifile" ]; then
  chmod 755 ../libstdc++/config/abi/{extractsym,makestub,makestub2,makeversym}
  ../libstdc++/config/abi/makeversym ../libstdc++/config/abi/$abifile \
    > ../libstdc++/sym_vers.map
  ../libstdc++/config/abi/makestub ../libstdc++/config/abi/$abifile \
    > libstdc++_stub.s
  ../libstdc++/config/abi/makestub2 ../libstdc++/config/abi/$abifile \
    > libstdc++_stub2.s
fi

make bootstrap-lean

cd ..

%install
rm -fr $RPM_BUILD_ROOT
export PATH=`pwd`/obj-%{_target_platform}/ld_hack/${PATH:+:$PATH}

strip -g obj-%{_target_platform}/gcc/libgcc.a
strip -g -R .comment obj-%{_target_platform}/gcc/crt*.o
# Create empty archive
ar rs libgcc_eh.a
mkdir -p $RPM_BUILD_ROOT%{_prefix}/%{_lib}/
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/gcc-lib/%{_target_platform}/%{gcc_version}
install -m 755 obj-%{_target_platform}/%{_target_platform}/libstdc++/libstdc++-3-libc6.2-2-2.10.0.so \
  $RPM_BUILD_ROOT%{_prefix}/%{_lib}/
install -m 644 obj-%{_target_platform}/gcc/libgcc.a \
  $RPM_BUILD_ROOT%{_prefix}/lib/gcc-lib/%{_target_platform}/%{gcc_version}/
install -m 644 libgcc_eh.a \
  $RPM_BUILD_ROOT%{_prefix}/lib/gcc-lib/%{_target_platform}/%{gcc_version}/
install -m 644 obj-%{_target_platform}/gcc/crt{begin,end}{,S}.o \
  $RPM_BUILD_ROOT%{_prefix}/lib/gcc-lib/%{_target_platform}/%{gcc_version}/
ln -sf libstdc++-3-libc6.2-2-2.10.0.so \
  $RPM_BUILD_ROOT%{_prefix}/%{_lib}/libstdc++-libc6.2-2.so.3

LIB_ARCH=`echo %{_target_cpu} | sed 's/i?86/i386/'`

%clean
rm -rf $RPM_BUILD_ROOT

%post -n compat-libstdc++-296 -p /sbin/ldconfig

%postun -n compat-libstdc++-296 -p /sbin/ldconfig

%files -n compat-libstdc++-296
%defattr(-,root,root)
%{_prefix}/%{_lib}/libstdc++-3-libc6.2-2-2.10.0.so
%{_prefix}/%{_lib}/libstdc++-libc6.2-2.so.3

%files -n compat-libgcc-296
%defattr(-,root,root)
%dir %{_prefix}/lib/gcc-lib
%dir %{_prefix}/lib/gcc-lib/%{_target_platform}
%dir %{_prefix}/lib/gcc-lib/%{_target_platform}/%{gcc_version}
%{_prefix}/lib/gcc-lib/%{_target_platform}/%{gcc_version}/libgcc.a
%{_prefix}/lib/gcc-lib/%{_target_platform}/%{gcc_version}/libgcc_eh.a
%{_prefix}/lib/gcc-lib/%{_target_platform}/%{gcc_version}/crtbegin.o
%{_prefix}/lib/gcc-lib/%{_target_platform}/%{gcc_version}/crtbeginS.o
%{_prefix}/lib/gcc-lib/%{_target_platform}/%{gcc_version}/crtend.o
%{_prefix}/lib/gcc-lib/%{_target_platform}/%{gcc_version}/crtendS.o

%changelog
* Mon May 17 2010 Jakub Jelinek  <jakub@redhat.com> 2.96-144
  - ensure libstdc++.so is linked with -Wl,-z,noexecstack (#592519)

* Mon Apr 26 2010 Dennis Gregorovic <dgregor@redhat.com> - 2.96-143.2
- Rebuilt for RHEL 6
Related: rhbz#566527

* Mon Apr 26 2010 Dennis Gregorovic <dgregor@redhat.com> - 2.96-143.1
- Rebuilt for RHEL 6
Related: rhbz#566527

* Tue Jul 28 2009 Jakub Jelinek  <jakub@redhat.com> 2.96-143
- replace -mtune=atom in $RPM_OPT_FLAGS with something that
  GCC 2.96-RH groks

* Mon Mar  9 2009 Jakub Jelinek  <jakub@redhat.com> 2.96-142
- rebuilt with GCC 4.4

* Tue Jul 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.96-141
- fix license tag
- fix patches to apply with fuzz=0

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.96-140
- Autorebuild for GCC 4.3

* Tue Oct  9 2007 Jakub Jelinek  <jakub@redhat.com> 2.96-139
- rebuilt

* Mon Aug 21 2006 Jakub Jelinek  <jakub@redhat.com> 2.96-138
- link ppc libstdc++.so against -lnldbl_nonshared

* Thu Aug 10 2006 Jakub Jelinek  <jakub@redhat.com> 2.96-137
- remove egcs 1.1.2 compat libraries, there have been plenty
  of warnings these will go away in the last 7 years

* Mon Jul 17 2006 Jakub Jelinek  <jakub@redhat.com> 2.96-136
- rebuilt

* Mon Feb 13 2006 Jakub Jelinek  <jakub@redhat.com> 2.96-135
- replace -mtune=generic in $RPM_OPT_FLAGS with something that
  GCC 2.96-RH groks

* Wed Jan  4 2006 Jakub Jelinek  <jakub@redhat.com> 2.96-134
- rebuilt against glibc-2.3.90-26 to pick up a sanitized
  <bits/libc-lock.h> (#176745)

* Sat Dec 17 2005 Jakub Jelinek  <jakub@redhat.com> 2.96-133
- rebuilt with new gcc, massage $RPM_OPT_FLAGS, as GCC 2.96-RH doesn't
  grok -fstack-protector etc.

* Tue Mar  8 2005 Jakub Jelinek  <jakub@redhat.com> 2.96-132.fc4
- new compatibility package
