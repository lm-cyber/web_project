import { useState } from 'react';
import { ru } from './i18n/ru.ts';
import { ContentWrapper } from '../../components/ContentWrapper';
import { Menu } from '../../components/Menu';
import { Title } from '../../components/UI/Text/Title';
import { Header } from '../../components/Header';
import { useGetProductsByTypeQuery } from '../../../core/api/product';
import { CatalogItem } from '../../components/UI/Card/CatalogItem';
import { Footer } from '../../components/Footer';

export const Catalog = () => {
    const [curTypeId, setCurTypeId] = useState<number | null>(null);
    const { data } = useGetProductsByTypeQuery(curTypeId ?? 0);

    return (
        <>
            <Header />
            <ContentWrapper>
                <div className={'mb-36 mt-5 grid grid-cols-12 gap-14'}>
                    <div className={'col-span-3 mt-20'}>
                        <Menu curTypeId={curTypeId} setCurTypeId={setCurTypeId} />
                    </div>
                    <div className={'col-span-9'}>
                        <Title name={ru.title} />
                        <div className={'flex flex-wrap gap-7'}>
                            {data?.map((x) => (
                                <CatalogItem key={x?.id} id={x?.id} title={x?.name} imageId={x?.images[0]?.id} />
                            ))}
                        </div>
                    </div>
                </div>
            </ContentWrapper>
            <Footer />
        </>
    );
};
