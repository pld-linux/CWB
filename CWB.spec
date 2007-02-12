Summary:	The Edinburgh Concurrency Workbench
Summary(pl.UTF-8):   Edinburgh - środowisko do badania współbieżności
Name:		CWB
Version:	7.1
Release:	1
License:	free for non-commercial
# http://www.dcs.ed.ac.uk/home/cwb/copyright.html
Group:		Development/Tools
# http://homepages.inf.ed.ac.uk/perdita/cwb/CWBEXPORTDIR/src.tar.gz
Source0:	src.tar.gz
# NoSource0-md5:	76eab4c6ccab3990b9d0e496dbf283e5
# http://www.dcs.ed.ac.uk/home/cwb/getting.html
Source1:	custom.ml
NoSource:	0
NoSource:	1
URL:		http://www.dcs.ed.ac.uk/home/cwb/
BuildRequires:	smlnj >= 110
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Edinburgh Concurrency Workbench (CWB) is an automated tool which
caters for the manipulation and analysis of concurrent systems. In
particular, the CWB allows for various equivalence, preorder and model
checking using a variety of different process semantics.

%description -l pl.UTF-8
Edinburgh Concurrency Workbench (CWB) to automatyczne narzędzie
obsługujące manipulowanie i analizę systemów współbieżnych. W
szczególności pozwala na różne równoważności, wstępne porządkowanie i
sprawdzanie modeli przy użyciu wielu różnych semantyk procesów.

%prep
%setup -q -n %{name}%{version}
install %{SOURCE1} .

%build
sml < custom.ml

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install cwb.x86-linux $RPM_BUILD_ROOT%{_datadir}/%{name}

cat <<EOF >$RPM_BUILD_ROOT%{_bindir}/cwb
#!/bin/sh
sml @SMLload=%{_datadir}/%{name}/cwb.x86-linux
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
