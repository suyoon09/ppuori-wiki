import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: '뿌리 — 건강기능식품 원료 사전',
  description: '우리가 먹는 모든 것에는 기원이 있습니다. 건강기능식품 원료의 뿌리를 찾아보세요.',
  openGraph: {
    title: '뿌리 — 건강기능식품 원료 사전',
    description: '우리가 먹는 모든 것에는 기원이 있습니다.',
    locale: 'ko_KR',
    type: 'website',
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ko">
      <body>
        {children}
        <footer className="footer">
          <p className="footer-text">
            본 사이트의 정보는 참고용이며, 의학적 진단이나 치료를 대체하지 않습니다.
            건강기능식품 섭취 전 전문가와 상담하세요.
          </p>
          <div className="footer-links">
            <a href="/about">소개</a>
            <a href="/">홈</a>
          </div>
        </footer>
      </body>
    </html>
  );
}
