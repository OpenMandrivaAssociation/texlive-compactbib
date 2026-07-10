%global tl_name compactbib
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Multiple thebibliography environments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/compactbib
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/compactbib.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Allows a second bibliography, optionally with a different title, after
the main bibliography.

