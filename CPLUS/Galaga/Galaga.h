
// Galaga.h : Galaga ���� ���α׷��� ���� �� ��� ����
//
#pragma once

#ifndef __AFXWIN_H__
	#error "PCH�� ���� �� ������ �����ϱ� ���� 'stdafx.h'�� �����մϴ�."
#endif

#include "resource.h"       // �� ��ȣ�Դϴ�.


// CGalagaApp:
// �� Ŭ������ ������ ���ؼ��� Galaga.cpp�� �����Ͻʽÿ�.
//

class CGalagaApp : public CWinAppEx
{
public:
	CGalagaApp();


// �������Դϴ�.
public:
	virtual BOOL InitInstance();
	virtual int ExitInstance();

// �����Դϴ�.
	afx_msg void OnAppAbout();
	DECLARE_MESSAGE_MAP()

private:
	ULONG_PTR m_gpToken;
};

extern CGalagaApp theApp;
