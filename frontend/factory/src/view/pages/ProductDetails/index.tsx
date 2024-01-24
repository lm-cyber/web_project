import { Link, useLocation, useNavigate } from 'react-router-dom';
import classNames from 'classnames';
import { ru } from './i18n/ru.ts';
import { ContentWrapper } from '../../components/ContentWrapper';
import { Menu } from '../../components/Menu';
import { Title } from '../../components/UI/Text/Title';
import { Header } from '../../components/Header';
import { useGetProductsByTypeQuery, useGetProductsQuery } from '../../../core/api/product';
import { CatalogFullItem } from '../../components/CatalogFullItem';
import styles from '../../components/CatalogPart/index.module.scss';
import { CatalogItem } from '../../components/UI/Card/CatalogItem';
import { Footer } from '../../components/Footer';

const cx = classNames.bind(styles);

export const ProductDetails = () => {
    const curTypeId = null;
    const { data: typesData } = useGetProductsByTypeQuery(curTypeId ?? 0);

    const location = useLocation();
    const navigate = useNavigate();
    const id = location.pathname.split('/')[2];
    const { data: productData } = useGetProductsQuery(id.toString());

    return (
        <>
            <Header />
            <ContentWrapper>
                <div className={'mb-28 mt-5 grid grid-cols-12 gap-14'}>
                    <div className={'col-span-3 mt-20'}>
                        <Menu isPieceOfShit={true} curTypeId={curTypeId} setCurTypeId={() => navigate('/catalog')} />
                    </div>
                    <div className={'col-span-9'}>
                        <Title name={ru.title} />
                        <div className={'flex flex-wrap gap-7'}>
                            {productData && (
                                <CatalogFullItem
                                    id={Number(id)}
                                    productName={productData[0]?.name}
                                    description={productData[0]?.description}
                                    img={productData[0]?.images[0]?.id}
                                />
                            )}
                        </div>
                        <div className={cx(styles.scrollable, styles.hideScrollBar)}>
                            <div className={cx(styles.cardsWrapper)}>
                                {typesData?.slice(0, 7)?.map((product) => (
                                    <Link key={product.id} to={`/catalog/${product.id}`}>
                                        <CatalogItem
                                            id={product.id}
                                            key={product?.id}
                                            title={product?.name}
                                            imageId={product?.images[0]?.id}
                                        />
                                    </Link>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            </ContentWrapper>
            <Footer />
        </>
    );
};
