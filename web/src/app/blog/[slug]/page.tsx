import Link from 'next/link';
import Nav from '@/components/Nav';
import { getPost, getPostSlugs } from '@/lib/blog-utils';
import type { Metadata } from 'next';

// Generate static paths at build time
export function generateStaticParams() {
    return getPostSlugs().map((slug) => ({ slug }));
}

// Dynamic metadata for SEO
export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
    const { slug } = await params;
    const post = getPost(slug);
    if (!post) return { title: '글을 찾을 수 없습니다 — 뿌리' };
    return {
        title: `${post.title} — 뿌리 탐구`,
        description: post.summary,
        keywords: post.keywords || post.tags.join(', '),
        openGraph: {
            title: post.title,
            description: post.summary,
            type: 'article',
            publishedTime: post.date,
            tags: post.tags,
            ...(post.thumbnail ? { images: [post.thumbnail] } : {}),
        },
    };
}

export default async function BlogPostPage({ params }: { params: Promise<{ slug: string }> }) {
    const { slug } = await params;
    const post = getPost(slug);

    if (!post) {
        return (
            <>
                <Nav />
                <div className="container detail-page" style={{ textAlign: 'center', paddingTop: '120px' }}>
                    <h1 style={{ fontWeight: 300, marginBottom: 16 }}>글을 찾을 수 없습니다</h1>
                    <Link href="/blog" style={{ color: '#666', borderBottom: '1px solid #ccc' }}>탐구로 돌아가기</Link>
                </div>
            </>
        );
    }

    return (
        <>
            <Nav />
            <article className="container detail-page blog-article" style={{ paddingTop: '100px' }}>
                {/* Breadcrumb */}
                <div className="detail-breadcrumb">
                    <Link href="/">홈</Link>{' / '}
                    <Link href="/blog">탐구</Link>{' / '}
                    <span>{post.title}</span>
                </div>

                {/* Header */}
                <header className="blog-article-header">
                    <span className="blog-article-category">{post.category}</span>
                    <h1 className="blog-article-title">{post.title}</h1>
                    <div className="blog-article-meta">
                        <time>{post.date}</time>
                        <span className="blog-article-reading">{post.readingTime}분 읽기</span>
                    </div>
                </header>

                {/* Thumbnail */}
                {post.thumbnail && (
                    <div className="blog-article-hero">
                        <img src={post.thumbnail} alt={post.title} />
                    </div>
                )}

                {/* Article content — rendered markdown */}
                <div
                    className="blog-article-content"
                    dangerouslySetInnerHTML={{ __html: post.contentHtml }}
                />

                {/* Tags */}
                {post.tags.length > 0 && (
                    <div className="blog-article-tags">
                        {post.tags.map((tag) => (
                            <span key={tag} className="blog-tag">#{tag}</span>
                        ))}
                    </div>
                )}

                {/* Related ingredients from our wiki */}
                {post.relatedIngredients && post.relatedIngredients.length > 0 && (
                    <section className="detail-section">
                        <h2>관련 원료 보기</h2>
                        <div className="blog-related-ingredients">
                            {post.relatedIngredients.map((ing) => (
                                <Link key={ing.id} href={`/ingredients/${ing.id}`} className="blog-related-link">
                                    {ing.name} →
                                </Link>
                            ))}
                        </div>
                    </section>
                )}

                {/* Back to blog */}
                <div style={{ textAlign: 'center', padding: '48px 0 24px' }}>
                    <Link href="/blog" className="blog-back-link">← 탐구 목록으로</Link>
                </div>
            </article>
        </>
    );
}
