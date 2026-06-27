/**
 * =====================================================
 * AI Empire Pro V8
 * Pagination Utilities
 * Datei: server/utils/pagination.js
 * =====================================================
 */

class Pagination {

    static parse(query = {}) {

        const page = Math.max(

            1,

            parseInt(query.page, 10) || 1

        );

        const limit = Math.min(

            100,

            Math.max(

                1,

                parseInt(query.limit, 10) || 20

            )

        );

        const skip = (page - 1) * limit;

        return {

            page,

            limit,

            skip

        };

    }

    static build({

        items = [],

        total = 0,

        page = 1,

        limit = 20

    }) {

        const pages = Math.max(

            1,

            Math.ceil(total / limit)

        );

        return {

            items,

            pagination: {

                page,

                limit,

                total,

                pages,

                hasNext:

                    page < pages,

                hasPrevious:

                    page > 1,

                nextPage:

                    page < pages

                        ? page + 1

                        : null,

                previousPage:

                    page > 1

                        ? page - 1

                        : null

            }

        };

    }

    static async mongoose(model, query = {}, options = {}) {

        const {

            page,

            limit,

            skip

        } = this.parse(options);

        const [items, total] = await Promise.all([

            model.find(query)

                .skip(skip)

                .limit(limit)

                .sort(options.sort || {}),

            model.countDocuments(query)

        ]);

        return this.build({

            items,

            total,

            page,

            limit

        });

    }

}

module.exports = Pagination;
