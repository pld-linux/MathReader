# TODO:
# - version for PPC/alpha/IA64/AMD64
# - talk with wolfram about redistribute it ;)
#
%define		_version	5.0.1
%define		ppc_version	4.2.1
Summary:	Mathematica Notebook Reader
Summary(pl):	Przegl�darka plik�w z programu Mathematica
Name:		MathReader
%ifnarch ppc
Version:	%{_version}
%else
Version:	%{ppc_version}
%endif
Release:	1.1
License:	almost free, distributable
# from http://www.wolfram.com/products/mathreader/download.cgi
Source0:	%{name}_%{_version}_Linux.sh
# Source0-md5:	35b7144eff51e017a03bf5c68d743548
# Source0-size:	9356911
Source1:	%{name}_%{_version}_Linux-AMD64.sh
# Source1-md5:	54c0db30f9a78269c03c970aaa841b66
# Source1-size:	10186360
Source2:	%{name}_%{_version}_Linux-AXP.sh
# Source2-md5:	9ab612c9543c69838dd38445dd0e8b05
# Source2-size:	10534517
Source3:	%{name}-%{ppc_version}-Linux-PPC.tar.gz
# Source3-md5:	9743cf3c81d3f83661034ae2cf5b6e78
# Source3-size:	9269016
Source4:	%{name}_%{_version}_Linux-IA64.sh
# Source4-md5:	6ea3a14eac68391da213a25d62c629d4
# Source4-size:	12019319
# based on http://www.wolfram.com/products/mathreader/licenseagreement.html
Source5:	%{name}-license.txt
Source6:	%{name}.desktop
Group:		Applications/Math
URL:		http://www.wolfram.com/products/mathreader/
ExclusiveArch:	%{ix86} ppc alpha amd64 ia64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MathReader is a viewer for notebook documents created with
Mathematica, the world's only fully integrated technical computing
system. MathReader lets you display and print Mathematica notebooks,
animate graphics, play sounds, and copy information from notebooks to
other documents. MathReader can be used by most web browsers as a
helper application for viewing notebook documents.

%description -l pl
MathReader jest przegl�dark� dla dokument�w utworzonych w programie
Mathematica, jedynym w �wiecie w pe�ni zintegrowanym systemie
technicznych oblicze�. MathReader pozwala wy�wietla� i drukowa�
notatki, odtwarza� animacje, odgrywa� d�wi�ki i kopiowa� informacje z
notatek programu Mathematica do innych dokument�w. MathReader mo�e by�
te� u�ywany przez wi�kszo�� przegl�darek WWW jako aplikacja pomocnicza
do przegl�dania dokument�w.

%prep

%install
rm -rf $RPM_BUILD_ROOT

%ifarch %{ix86}
%define _source	%{SOURCE0}
%endif
%ifarch amd64
%define	_source	%{SOURCE1}
%endif
%ifarch alpha
%define	_source	%{SOURCE2}
%endif
#%%ifarch ia64
#%%define	_source	%{SOURCE4}
#%%endif

%ifnarch ppc
sh %{_source} auto \
	-targetdir=$RPM_BUILD_ROOT%{_libdir}/%{name} \
	-execdir=$RPM_BUILD_ROOT%{_bindir}
%else
TODO
%endif
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}
ln -sf %{_libdir}/%{name}/Executables/{MathReader,mathreader} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE5} .
install %{SOURCE6} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}-license.txt
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/Executables
%{_libdir}/%{name}/Configuration
%{_libdir}/%{name}/Documentation
%dir %{_libdir}/%{name}/SystemFiles
%{_libdir}/%{name}/SystemFiles/CharacterEncodings
%dir %{_libdir}/%{name}/SystemFiles/FrontEnd
%dir %{_libdir}/%{name}/SystemFiles/FrontEnd/Binaries
%ifarch %{ix86}
%attr(755,root,root) %{_libdir}/%{name}/SystemFiles/FrontEnd/Binaries/Linux
%endif
%ifarch amd64
%attr(755,root,root) %{_libdir}/%{name}/SystemFiles/FrontEnd/Binaries/Linux-x86-64
%endif
%ifarch alpha
%attr(755,root,root) %{_libdir}/%{name}/SystemFiles/FrontEnd/Binaries/Linux-AXP
%endif
%{_libdir}/%{name}/SystemFiles/FrontEnd/StyleSheets
%{_libdir}/%{name}/SystemFiles/FrontEnd/SystemResources
%{_libdir}/%{name}/SystemFiles/FrontEnd/TextResources
%{_libdir}/%{name}/SystemFiles/Fonts
%{_libdir}/%{name}/SystemFiles/Installation
%{_libdir}/%{name}/SystemFiles/SpellingDictionaries
%{_desktopdir}/%{name}.desktop
