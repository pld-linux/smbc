Summary:	Simple Samba Commander
Summary(pl):	Konsolowa przegl�darka otoczenia sieciowego
Name:		smbc
Version:	0.7.2
Release:	0.1
License:	GPL
Group:		Applications/Networking	
Source0:	http://www.air.rzeszow.pl/smbc/smbc/current/%{name}-%{version}.tgz
# Source0-md5:	678700ce4c7390bab77555089e98d5ce
Patch0:		%{name}-ncurses.patch
URL:		http://freshmeat.net/projects/sambacommander/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libsmbclient-devel >= 3.0
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple Samba Commander is a text mode SMBnet commander. In SMBC, you
can browse the local network or you can use the search function to
find the files. You can also download and upload files or all
directories to your computer or create remote and local directories.
SMBC has a resume function and supports UTF-8 characters.

%description -l pl
Simple Samba Commander jest prost� tekstow� przegl�dark� sieci opartej
o protok� SMB. Za pomoc� SMBC mo�na przegl�da� sie� lokaln� lub w
poszukiwaniu konkretnego pliku wykorzysta� funkcj� wyszukiwania.
Dost�pna jest r�wnie� funkcja pobierania oraz wysy�ania plik�w jak i
ca�ych katalog�w. SMBC zawiera funkcje automatycznego wznawiania
po��czenia, obs�ug� wielu j�zyk�w wspiera r�wnie� standard kodowania
znak�w UTF8.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/locale/pl/LC_MESSAGES}

install src/smbc $RPM_BUILD_ROOT%{_bindir}
install src/smbc-utf-x $RPM_BUILD_ROOT%{_bindir}
install po/pl.gmo $RPM_BUILD_ROOT%{_datadir}/locale/pl/LC_MESSAGES/smbc.mo

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc FAQ README doc/sample.smbcrc
%attr(755,root,root) %{_bindir}/*
