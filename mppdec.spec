# $Revision: 1.1 $ 
Summary:	Tool for decompressing mpc files
Summary(pl):	Program do dekompresji plików mpc
Name:		mppdec
Version:	1.1
Release:	0
License:	GPL
Group:		Applications/Multimedia
Source0:	http://www.personal.uni-jena.de/~pfk/MPP/src/%{name}-%{version}.tar.bz2
# Source0-md5:	53172eef6b409725b885ca39f98a56bc
Patch0:		%{name}-makefile.patch
URL:		 http://www.uni-jena.de/~pfk/mpp/
#BuildRequires:	libvorbis-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a speed and portability optimized version of Andree Buschmann's
MPEG-Plus decoder. Speed enhancement is about 1:4...1:5 relative to the
original source. Some of these optimizations flood back to the original
decoder, but especially on AMD K6-2/AMD K6-III/AMD Athlon/AMD Duron/Intel
Pentium III/Intel Pentium 4 there's still some hand written assembler code
so this decoder ist still much faster.


%description -l pl
Jest to ulepszona i przeno¶na wersja MPEG-Plus decoder autorstwa Andree 
Buschmann. 

%prep
%setup -q
%patch -p0

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/bin/
install mppdec $RPM_BUILD_ROOT/usr/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
#%{_mandir}/man1/*
