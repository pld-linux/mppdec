# $Revision: 1.8 $ 
#
# Conditional build:
%bcond_without	esd	# without EsounD support
#
Summary:	Tool for decompressing MPC files
Summary(pl):	Program do dekompresji plików MPC
Name:		mppdec
Version:	1.1
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://www.personal.uni-jena.de/~pfk/MPP/src/%{name}-%{version}.tar.bz2
# Source0-md5:	53172eef6b409725b885ca39f98a56bc
Patch0:		%{name}-makefile.patch
URL:		http://www.uni-jena.de/~pfk/mpp/
%{?with_esd:BuildRequires:esound-devel}
BuildRequires:	sed >= 4.0
BuildRequires:	nasm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a speed and portability optimized version of Andree
Buschmann's MPEG-Plus decoder. Speed enhancement is about 1:4...1:5
relative to the original source. Some of these optimizations flood
back to the original decoder, but especially on AMD K6-2, AMD K6-III,
AMD Athlon, AMD Duron, Intel Pentium III, Intel Pentium 4 there's
still some hand written assembler code so this decoder is still much
faster.

%description -l pl
Jest to zoptymalizowana pod k±tem szybko¶ci i przeno¶no¶ci wersja
dekodera MPEG-Plus autorstwa Andree Buschmanna. Poprawa szybko¶ci
wynosi 1:4...1:5 w stosunku do oryginalnych ¼róde³. Niektóre
optymalizacje pochodz± z oryginalnego dekodera, ale szczególnie dla
procesorów AMD K6-2, AMD K6-III, AMD Athlon, AMD Duron, Intel Pentium
II, Intel Pentium 4 jest trochê rêcznie napisanego w asemblerze kodu,
wiêc dekoder jest nadal du¿o szybszy.

%prep
%setup -q
%patch0 -p1

# don't want static binaries
grep -v -e '-static' Makefile > Makefile.nostatic
%if ! %{with esd}
%{__sed} -i -e 's,-lesd,,g' Makefile.nostatic
grep -v "USE_ESD_AUDIO" mpp.h >> mpp.h.1
mv mpp.h{.1,}
%endif 

# gcc4 fix (unrecognized option error)
sed -i -e 's/-fmove-all-movables//' Makefile.nostatic

%build
%{__make} mppdec -f Makefile.nostatic \
	CC="%{__cc} -pipe" \
	ARCH="%{rpmcflags}" \
%ifarch i586 i686 athlon
	PENTIUM=1
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install mppdec $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
