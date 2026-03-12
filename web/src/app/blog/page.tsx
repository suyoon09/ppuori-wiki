import Link from 'next/link';
import Nav from '@/components/Nav';
import { getAllPosts } from '@/lib/blog-utils';

export const metadata = {
    title: '탐구 — 뿌리 | 건강기능식품 원료 이야기',
    description: '건강기능식품 원료의 과학적 근거와 일상 건강 상식을 알기 쉽게 전달합니다. 비타민, 미네랄, 프로바이오틱스 등 원료 이야기.',
    keywords: '건강기능식품, 비타민, 미네랄, 건강상식, 원료, 영양제',
};

export default function BlogIndexPage() {
    const posts = getAllPosts();
    const featured = posts[0];
    const rest = posts.slice(1);

    return (
        <>
            <Nav />
            <main className="magazine-page">
                {/* Magazine header */}
                <header className="magazine-header">
                    <div className="magazine-header-inner">
                        <span className="magazine-label">탐구</span>
                        <h1 className="magazine-title">원료의 과학,<br />일상의 건강</h1>
                        <p className="magazine-subtitle">
                            근거 기반 건강 정보와 원료 이야기를 전합니다.
                        </p>
                    </div>
                </header>

                {posts.length === 0 ? (
                    <section className="magazine-empty">
                        <p>아직 등록된 글이 없습니다.</p>
                    </section>
                ) : (
                    <div className="magazine-content">
                        {/* Featured article — full-width hero */}
                        {featured && (
                            <Link href={`/blog/${featured.slug}`} className="magazine-feature">
                                <div className="magazine-feature-image">
                                    {featured.thumbnail && (
                                        <img src={featured.thumbnail} alt={featured.title} loading="eager" />
                                    )}
                                    <div className="magazine-feature-overlay" />
                                </div>
                                <div className="magazine-feature-content">
                                    <span className="magazine-feature-category">{featured.category}</span>
                                    <h2 className="magazine-feature-title">{featured.title}</h2>
                                    <p className="magazine-feature-summary">{featured.summary}</p>
                                    <div className="magazine-feature-meta">
                                        <time>{featured.date}</time>
                                        <span className="magazine-dot">·</span>
                                        <span>{featured.readingTime}분 읽기</span>
                                    </div>
                                </div>
                            </Link>
                        )}

                        {/* Editorial grid — remaining articles */}
                        {rest.length > 0 && (
                            <section className="magazine-grid-section">
                                <div className="magazine-grid">
                                    {rest.map((post) => (
                                        <Link key={post.slug} href={`/blog/${post.slug}`} className="magazine-card">
                                            {post.thumbnail && (
                                                <div className="magazine-card-image">
                                                    <img src={post.thumbnail} alt={post.title} loading="lazy" />
                                                </div>
                                            )}
                                            <div className="magazine-card-body">
                                                <span className="magazine-card-category">{post.category}</span>
                                                <h3 className="magazine-card-title">{post.title}</h3>
                                                <p className="magazine-card-summary">{post.summary}</p>
                                                <div className="magazine-card-meta">
                                                    <time>{post.date}</time>
                                                    <span className="magazine-dot">·</span>
                                                    <span>{post.readingTime}분 읽기</span>
                                                </div>
                                            </div>
                                        </Link>
                                    ))}
                                </div>
                            </section>
                        )}
                    </div>
                )}
            </main>
        </>
    );
}
