# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/compactbib/compactbib.sty
# catalog-date 2007-01-01 11:39:06 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-compactbib
Version:	20070101
Release:	1
Summary:	Multiple thebibliography environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/compactbib/compactbib.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/compactbib.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Allows a second bibliography, optionally with a different
title, after the main bibliography.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/compactbib/compactbib.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
