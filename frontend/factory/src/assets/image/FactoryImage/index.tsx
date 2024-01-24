import React from 'react';
import classNames from 'classnames';
import styles from './index.module.scss';
import { ContentWrapper } from '../../../view/components/ContentWrapper';

const cx = classNames.bind(styles);

export const FactoryImage: React.FC = () => {
    return (
        <ContentWrapper>
            <img className={cx(styles.image)} src={'https://i.ibb.co/ySdhpgX/factory.jpg'} alt={'factory'} />
        </ContentWrapper>
    );
};
