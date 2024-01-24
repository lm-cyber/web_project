import React from 'react';

interface IBenefitCardProps {
    name: string;
    description: string;
}
export const BenefitCard: React.FC<IBenefitCardProps> = (props) => {
    return (
        <div
            className={
                // eslint-disable-next-line max-len
                'relative h-full w-full flex-col content-between rounded-[20px] bg-lightGray px-4 py-6 hover:bg-darkBlue hover:text-white'
            }
        >
            <div className={'text-[28px] font-medium'}>{props.name}</div>
            <div className={'absolute bottom-6 text-[19px]'}>{props.description}</div>
        </div>
    );
};
